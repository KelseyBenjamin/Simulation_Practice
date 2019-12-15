/*
 * Trick
 * 2016 (c) National Aeronautics and Space Administration (NASA)
 */

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Graphics;
import java.awt.RenderingHints;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.util.*;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.sound.sampled.*;
import java.net.URL;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
/**
 *
 * @author penn
 */


class ScenePoly {
    public Color color;
    public int n;
    public double[] x;
    public double[] y;
}


class RangeView extends JPanel {

    private int scale;
    private Color skyColor;
    private Color groundColor;

    private Color landerColor;

    private Color[] explosionColors;
    private int     explosionColors_n;

    // Origin of world coordinates in jpanel coordinates.
    private int worldOriginX;
    private int worldOriginY;

    private double[] landerPos;
    private double[] landerVel;
    private double   landerAngle;
    private double   landerAngleRate;
    private int      landerThrottle;    /* percent */

    private double   explosionSize;
    private double[] explosionPos;

    private double[] explosion_poly_x, explosion_poly_y;
    private int explosion_poly_n;

    private ScenePoly left_pad, right_pad;
    private ScenePoly left_L1,  right_L1;
    private ScenePoly left_L2,  right_L2;
    private ScenePoly left_L3,  right_L3;
    private ScenePoly left_L4,  right_L4;
    private ScenePoly fuselage;
    private ScenePoly nozzle;
    private ScenePoly left_rcs_pod, right_rcs_pod;
    private ScenePoly left_top_rcs_nozzle, right_top_rcs_nozzle, left_bottom_rcs_nozzle, right_bottom_rcs_nozzle;
    private ScenePoly docking_ring;
    private ScenePoly flame;

    private int[] workPolyX, workPolyY;



    // Controls
    private int throttleDelta ;
    private int rcs_state;
    private boolean Auto_1;
    private boolean Auto_2;


    /**
     * Class constructor.
     */
    public RangeView( int mapScale) {

        setScale(mapScale);

        throttleDelta = 0;
        rcs_state = 0;
        Auto_1 = false;
        Auto_2 = false;

        skyColor    = new Color(0,0,20);
        groundColor = new Color(150,150,150);
        landerColor = new Color(150,10,10);

        explosionColors = new Color[]
            { new Color(255,  63,   3),
              new Color(255, 127,  15),
              new Color(255, 191,  63),
              new Color(255, 255, 255) };
        explosionColors_n = 4;
        explosionSize = 0.0;
        explosionPos = new double[]
            { 5.0800, 0.0000};

        landerAngle = 0.0;
        landerPos  = new double[]
            {5.0, 0.0};
        landerVel  = new double[]
            {0.0, 0.0};
        landerThrottle = 0;

        left_pad = new ScenePoly();
        left_pad.color = new Color(200,200,150);
        left_pad.x = new double[] { -2.0, -1.6, -1.7, -1.8, -1.9, -2.0, -2.1, -2.2, -2.3, -2.4 };
        left_pad.y  = new double[] { -1.7, -1.7, -1.75, -1.77, -1.79, -1.80, -1.79, -1.77, -1.75, -1.70 };
        left_pad.n = 10;

        right_pad = new ScenePoly();
        right_pad.color = new Color(200,200,150);
        right_pad.x = new double[] { 2.0, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4 };
        right_pad.y = new double[] { -1.7, -1.7, -1.75, -1.77, -1.79, -1.80, -1.79, -1.77, -1.75, -1.70 };
        right_pad.n = 10;

        left_L1 = new ScenePoly();
        left_L1.color = new Color(100,100,100);
        left_L1.x = new double[]  { -1.46, -1.0,  -1.0, -1.48 };
        left_L1.y  = new double[] { -0.51, -0.95, -1.0, -0.55};
        left_L1.n = 4;

        right_L1 = new ScenePoly();
        right_L1.color = new Color(100,100,100);
        right_L1.x = new double[]  { 1.46, 1.0,  1.0, 1.48 };
        right_L1.y  = new double[] { -0.51, -0.95, -1.0, -0.55};
        right_L1.n = 4;

        left_L2 = new ScenePoly();
        left_L2.color = new Color(100,100,100);
        left_L2.x = new double[]  { -1.0, -1.0, -1.75, -1.84};
        left_L2.y  = new double[] { -0.95, -1.0, -1.28,-1.25};
        left_L2.n = 4;

        right_L2 = new ScenePoly();
        right_L2.color = new Color(100,100,100);
        right_L2.x = new double[]  { 1.0, 1.0, 1.75, 1.84};
        right_L2.y  = new double[] { -0.95, -1.0, -1.28,-1.25};
        right_L2.n = 4;

        left_L3 = new ScenePoly();
        left_L3.color = new Color(50,50,50);
        left_L3.x = new double[]  { -1.0,  -1.0,  -1.47, -1.75, -1.84, -1.54};
        left_L3.y  = new double[] { -0.15, -0.25, -0.53, -1.28, -1.25, -0.46};
        left_L3.n = 6;

        right_L3 = new ScenePoly();
        right_L3.color = new Color(50,50,50);
        right_L3.x = new double[] {   1.0,   1.0,  1.47,  1.75,  1.84,  1.54};
        right_L3.y = new double[] { -0.15, -0.25, -0.53, -1.28, -1.25, -0.46};
        right_L3.n = 6;

        left_L4 = new ScenePoly();
        left_L4.color = new Color(100,100,100);
        left_L4.x = new double[]  { -1.78, -1.94, -1.98, -1.81};
        left_L4.y  = new double[] { -1.27, -1.7, -1.7, -1.26};
        left_L4.n = 4;

        right_L4 = new ScenePoly();
        right_L4.color = new Color(100,100,100);
        right_L4.x = new double[]  { 1.78, 1.94, 1.98, 1.81};
        right_L4.y  = new double[] { -1.27, -1.7, -1.7, -1.26};
        right_L4.n = 4;

        fuselage = new ScenePoly();
        fuselage.color = new Color(200,200,220);
        fuselage.x = new double[]  { 0.40, 0.65, 0.90, 1.00,  1.00, -1.00, -1.00, -0.90, -0.65, -0.40};
        fuselage.y  = new double[] { 1.75, 1.60, 1.30, 0.85, -1.00, -1.00,  0.85,  1.30,  1.60,  1.75};
        fuselage.n = 10;

        nozzle = new ScenePoly();
        nozzle.color = new Color(150,150,150);
        nozzle.x = new double[]  { -0.3, -0.4, 0.4, 0.3};
        nozzle.y  = new double[] { -1.0, -1.3, -1.3, -1.0};
        nozzle.n = 4;

        left_rcs_pod = new ScenePoly();
        left_rcs_pod.color = new Color(100,100,100);
        left_rcs_pod.x = new double[]  { -1.0, -1.25, -1.25, -1.0};
        left_rcs_pod.y  = new double[] { 0.1, 0.1, -0.1, -0.1};
        left_rcs_pod.n = 4;

        right_rcs_pod = new ScenePoly();
        right_rcs_pod.color = new Color(100,100,100);
        right_rcs_pod.x = new double[]  { 1.0, 1.25, 1.25, 1.0};
        right_rcs_pod.y  = new double[] { 0.1, 0.1, -0.1, -0.1};
        right_rcs_pod.n = 4;

        left_top_rcs_nozzle = new ScenePoly();
        left_top_rcs_nozzle.color = new Color(255,100,100);
        left_top_rcs_nozzle.x = new double[]  { -1.12, -1.18, -1.2, -1.1 };
        left_top_rcs_nozzle.y  = new double[] { 0.1, 0.1, 0.2, 0.2 };
        left_top_rcs_nozzle.n = 4;

        right_top_rcs_nozzle = new ScenePoly();
        right_top_rcs_nozzle.color = new Color(255,100,100);
        right_top_rcs_nozzle.x = new double[]  { 1.12, 1.18, 1.2, 1.1 };
        right_top_rcs_nozzle.y  = new double[] { 0.1, 0.1, 0.2, 0.2 };
        right_top_rcs_nozzle.n = 4;

        left_bottom_rcs_nozzle = new ScenePoly();
        left_bottom_rcs_nozzle.color = new Color(255,100,100);
        left_bottom_rcs_nozzle.x = new double[]  { -1.12, -1.18, -1.2, -1.1 };
        left_bottom_rcs_nozzle.y  = new double[] { -0.1, -0.1, -0.2, -0.2 };
        left_bottom_rcs_nozzle.n = 4;

        right_bottom_rcs_nozzle = new ScenePoly();
        right_bottom_rcs_nozzle.color = new Color(255,100,100);
        right_bottom_rcs_nozzle.x = new double[]  { 1.12, 1.18, 1.2, 1.1 };
        right_bottom_rcs_nozzle.y  = new double[] { -0.1, -0.1, -0.2, -0.2 };
        right_bottom_rcs_nozzle.n = 4;

        docking_ring = new ScenePoly();
        docking_ring.color = new Color(100,100,200);
        docking_ring.x = new double[]  { 0.4, 0.4, -0.4, -0.4 };
        docking_ring.y  = new double[] { 2.0, 1.75, 1.75, 2.0 };
        docking_ring.n = 4;

        flame = new ScenePoly();
        flame.color = new Color(200,150,100);
        flame.x = new double[]  { 0.0, -0.4, 0.4 };
        flame.y  = new double[] { -6.3, -1.3, -1.3 };
        flame.n = 3;

        // Explosion polygon
        explosion_poly_x = new double[]
            { 0.0178, 0.0246, 0.0160, 0.0198, 0.0112, 0.0109, 0.0041, 0.0000,-0.0041,-0.0109,
             -0.0112,-0.0198,-0.0160,-0.0246,-0.0178,-0.0246,-0.0160,-0.0198,-0.0112,-0.0109,
             -0.0041, 0.0000, 0.0041, 0.0109, 0.0112, 0.0198, 0.0160, 0.0246, 0.0178};
        explosion_poly_y = new double[]
            { 0.0000, 0.0056, 0.0076, 0.0157, 0.0140, 0.0229, 0.0173, 0.0254, 0.0173, 0.0229,
              0.0140, 0.0157, 0.0076, 0.0056, 0.0000,-0.0056,-0.0076,-0.0157,-0.0140,-0.0229,
             -0.0173,-0.0254,-0.0173,-0.0229,-0.0140,-0.0157,-0.0076,-0.0056, 0.0000};
        explosion_poly_n = 29;

        workPolyX = new int[30];
        workPolyY = new int[30];
    }

    public void drawScenePoly(Graphics2D g, ScenePoly p, double angle_r , double x, double y) {
        // double angle_r =  Math.toRadians(angle_d);
        for (int ii = 0; ii < p.n; ii++) {
            workPolyX[ii] = (int)(worldOriginX + scale *
                ( Math.cos(angle_r) * p.x[ii] - Math.sin(angle_r) * p.y[ii] + x));
            workPolyY[ii] = (int)(worldOriginY - scale *
                ( Math.sin(angle_r) * p.x[ii] + Math.cos(angle_r) * p.y[ii] + y));
        }
        g.setPaint(p.color);
        g.fillPolygon(workPolyX, workPolyY, p.n);
    }

    public void rcs_ccw()           { rcs_state = 1; }
    public void rcs_cw()            { rcs_state = -1; }
    public void rcs_zero()          { rcs_state = 0; }
    public int get_rcs_state()      { return rcs_state; }

    public void throttleUp()        { throttleDelta =   1; }
    public void throttleDown()      { throttleDelta =  -1; }
    public void throttleZeroDelta() { throttleDelta =   0; }
    public int  getThrottleDelta()  { return throttleDelta; }

    public boolean getAuto_1()      { return Auto_1; }
    public void toggleAuto_1()      { Auto_1 = !Auto_1; }
    public boolean getAuto_2()      { return Auto_2; }
    public void toggleAuto_2()      { Auto_2 = !Auto_2; }

    public void setLanderAngle(double angle_r) {
        landerAngle = angle_r;
    }
    public void setLanderAngleRate(double angle_rate) {
        landerAngleRate = angle_rate;
    }
    public void setLanderPos(double x, double y) {
        landerPos[0] = x;
        landerPos[1] = y;
    }
    public void setLanderVel(double vx, double vy) {
        landerVel[0] = vx;
        landerVel[1] = vy;
    }
    public void setLanderThrottle(int percent) {
        landerThrottle = percent;
    }
    public void setExplosionSize(double size) {
        explosionSize = size;
    }
    public void setExplosionPos(double x, double y) {
        explosionPos[0] = x;
        explosionPos[1] = y;
    }
    public void setScale (int mapScale) {
        if (mapScale < 4) {
            scale = 4;
        } else if (mapScale > 128) {
            scale = 128;
        } else {
            scale = mapScale;
        }
        repaint();
    }

    public int getScale() {
        return scale;
    }

    public void drawCenteredCircle(Graphics2D g, int x, int y, int d) {
        x = x-(d/2);
        y = y-(d/2);
        g.fillOval(x,y,d,d);
    }


    private void doDrawing(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;

        RenderingHints rh = new RenderingHints(
                RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        rh.put(RenderingHints.KEY_RENDERING,
               RenderingHints.VALUE_RENDER_QUALITY);

        int ii, jj;
        int width  = getWidth();
        int height = getHeight();

        worldOriginX = (width/2)  - (int)(scale * landerPos[0]);
        worldOriginY = (height/2) + (int)(scale * landerPos[1]);

        // Draw Sky
        g2d.setPaint(skyColor);
        g2d.fillRect(0, 0, width, worldOriginY);

        // |jpanel_x| = |origin_x| + |scale    0  | * |cos(angle) -sin(angle)| * |world_x|
        // |jpanel_y|   |origin_y|   |  0   -scale|   |sin(angle)  cos(angle)|   |world_y|

        // Draw explosion.
        if ( explosionSize > 0.0 ) {
            for (jj = 0; jj < explosionColors_n ; jj ++) {
                for (ii = 0; ii < explosion_poly_n ; ii ++) {
                    double ex = explosionSize * (explosionColors_n - jj) * explosion_poly_x[ii];
                    double ey = explosionSize * (explosionColors_n - jj) * explosion_poly_y[ii];
                    workPolyX[ii] = (int)(worldOriginX + scale * (ex + explosionPos[0] ));
                    workPolyY[ii] = (int)(worldOriginY - scale * (ey + explosionPos[1] ));
                }
                g2d.setPaint(explosionColors[jj]);
                g2d.fillPolygon(workPolyX, workPolyY, explosion_poly_n);
            }
        }

        // Draw ground.
        g2d.setPaint(groundColor);
        g2d.fillRect(0, worldOriginY, width, height);

        // ===============================================================================
        //  Draw lander
        // ===============================================================================
        drawScenePoly(g2d, left_pad, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, right_pad, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, left_L1, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, right_L1, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, left_L2, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, right_L2, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, left_L3, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, right_L3, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, left_L4, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, right_L4, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, fuselage, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, nozzle, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, left_rcs_pod, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, right_rcs_pod, landerAngle, landerPos[0], landerPos[1]);

        drawScenePoly(g2d, left_top_rcs_nozzle, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, right_top_rcs_nozzle, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, left_bottom_rcs_nozzle, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, right_bottom_rcs_nozzle, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, docking_ring, landerAngle, landerPos[0], landerPos[1]);
        drawScenePoly(g2d, flame, landerAngle, landerPos[0], landerPos[1]);

        // ===============================================================================
        // Move the first vertex of the triangular polygon that represents the main-engine
        // plume to make the triangle bigger or smaller depending on the throttle setting.
        flame.y[0] = - (landerThrottle / 100.0) * 5.0 - 1.3;

        for (ii = 0; ii < flame.n; ii++) {
            workPolyX[ii] = (int)(worldOriginX + scale *
                ( Math.cos(landerAngle) * flame.x[ii] - Math.sin(landerAngle) * flame.y[ii] + landerPos[0] ));
            workPolyY[ii] = (int)(worldOriginY - scale *
                ( Math.sin(landerAngle) * flame.x[ii] + Math.cos(landerAngle) * flame.y[ii] + landerPos[1] ));
        }
        g2d.setPaint(flame.color);
        g2d.fillPolygon(workPolyX, workPolyY, flame.n);

        // Draw range markers.
        int tickRange = 50;
        if (scale >=  8) tickRange = 20;
        if (scale >= 16) tickRange = 10;
        if (scale >= 32) tickRange =  5;
        if (scale >= 64) tickRange =  1;

        int lower = ((int)((      - worldOriginX)/(scale * tickRange)) + 1) * tickRange;
        int upper = ((int)((width - worldOriginX)/(scale * tickRange)) + 1) * tickRange;

        g2d.setPaint(Color.WHITE);

        for (ii = lower ; ii < upper ; ii += tickRange) {
            int mx = (int)(worldOriginX + scale * ii);
            g2d.drawLine( mx, worldOriginY, mx, worldOriginY + 20);
            g2d.drawString ( String.format("%d",ii), mx, worldOriginY + 15);
        }
        double angle_d =  landerAngle * 57.29577;
        double angle_rate_d = landerAngleRate * 57.29577;
        g2d.drawString ( String.format("SCALE: %d pixels/meter",scale), 20,20);
        g2d.drawString ( String.format("Throttle : [%d]", landerThrottle), 20,40);
        g2d.drawString ( String.format("Lander Angle (Deg): [%.2f]", angle_d), 20,60);
        g2d.drawString ( String.format("Lander AngleRate (Deg/s): [%.2f]", angle_rate_d), 20,80);
        g2d.drawString ( String.format("Lander Pos: [%.2f, %.2f]", landerPos[0], landerPos[1]), 20,100);
        g2d.drawString ( String.format("Lander Vel: [%.2f, %.2f]", landerVel[0], landerVel[1]), 20,120);

    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        doDrawing(g);
    }
}

class TrickSimMode {
    public static final int INIT = 0;
    public static final int FREEZE = 1;
    public static final int RUN = 5;
}

class ButtonPanel extends JPanel implements ActionListener {

    private LanderDisplay landerDisplay;
    private JButton zoomOutButton, zoomInButton;
    private JButton rollLeftButton, rollRightButton;
    private JButton throttleUpButton, throttleDownButton;
    private JButton Auto_1_Button, Auto_2_Button;

    public ButtonPanel(LanderDisplay disp) {
        landerDisplay = disp;
        setLayout(new BoxLayout(this, BoxLayout.X_AXIS));

        rollLeftButton = new JButton("\u21ba");
        rollLeftButton.addActionListener(this);
        rollLeftButton.setActionCommand("rollLeft");
        rollLeftButton.setToolTipText("Roll Left");
        add(rollLeftButton);

        throttleUpButton = new JButton("\u25b2");
        throttleUpButton.addActionListener(this);
        throttleUpButton.setActionCommand("throttleUp");
        throttleUpButton.setToolTipText("Throttle Up");
        add(throttleUpButton);

        throttleDownButton = new JButton("\u25bc");
        throttleDownButton.addActionListener(this);
        throttleDownButton.setActionCommand("throttleDown");
        throttleDownButton.setToolTipText("Throttle Down");
        add(throttleDownButton);

        rollRightButton = new JButton("\u21bb");
        rollRightButton.addActionListener(this);
        rollRightButton.setActionCommand("rollRight");
        rollRightButton.setToolTipText("Roll Right");
        add(rollRightButton);

        zoomOutButton = new JButton("Zoom Out");
        zoomOutButton.addActionListener(this);
        zoomOutButton.setActionCommand("zoomout");
        zoomOutButton.setToolTipText("Zoom Out");
        add(zoomOutButton);

        zoomInButton = new JButton("Zoom In");
        zoomInButton.addActionListener(this);
        zoomInButton.setActionCommand("zoomin");
        zoomInButton.setToolTipText("Zoom In");
        add(zoomInButton);

        Auto_1_Button = new JButton("Auto 1");
        Auto_1_Button.addActionListener(this);
        Auto_1_Button.setActionCommand("toggle_Auto_1");
        Auto_1_Button.setForeground(Color.BLACK);
        Auto_1_Button.setOpaque(true);
        add(Auto_1_Button);

        Auto_2_Button = new JButton("Auto_2");
        Auto_2_Button.addActionListener(this);
        Auto_2_Button.setActionCommand("toggle_Auto_2");
        Auto_2_Button.setForeground(Color.BLACK);
        add(Auto_2_Button);
    }

    public void actionPerformed(ActionEvent e) {
        String s = e.getActionCommand();
        switch (s) {
            case "rollLeft":
                landerDisplay.rcs_ccw();
                break;
            case "rollRight":
                landerDisplay.rcs_cw();
                break;
            case "throttleUp":
                landerDisplay.throttleUp();
                break;
            case "throttleDown":
                landerDisplay.throttleDown();
                break;
            case "zoomout":
                landerDisplay.setScale( landerDisplay.getScale() / 2 );
                break;
            case "zoomin":
                landerDisplay.setScale( landerDisplay.getScale() * 2 );
                break;
            case "toggle_Auto_1":
                landerDisplay.toggleAuto_1();
                if (landerDisplay.getAuto_1())
                    Auto_1_Button.setForeground(Color.GREEN);
                else
                    Auto_1_Button.setForeground(Color.BLACK);
                break;
            case "toggle_Auto_2":
                landerDisplay.toggleAuto_2();
                if (landerDisplay.getAuto_2())
                    Auto_2_Button.setForeground(Color.GREEN);
                else
                    Auto_2_Button.setForeground(Color.BLACK);
                break;
            default:
                System.out.println("Unknown Action Command:" + s);
                break;
        }
    }
} // class ButtonPanel

public class LanderDisplay extends JFrame {

    private RangeView rangeView;
    private BufferedReader in;
    private DataOutputStream out;
    private JPanel panelGroup0;
    private JPanel panelGroup1;
    private ButtonPanel buttonPanel;

    public enum SoundEffect {
        EXPLOSION("Explosion.wav"),
        CANNONBOOM("CannonBoom.wav");

        private Clip clip;

        SoundEffect(String soundFileName) {
            try {
            URL url = this.getClass().getClassLoader().getResource(soundFileName);
            AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(url);
            clip = AudioSystem.getClip();
            clip.open(audioInputStream);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        public void play() {
            if (clip.isRunning()) clip.stop();
            clip.setFramePosition(0);
            clip.start();
        }

        static void init() {
            values();
        }
    }

    public LanderDisplay(RangeView arena) {
        setTitle("Lander Range");

        rangeView  = arena;

        panelGroup1 = new JPanel();
        panelGroup1.setLayout(new BoxLayout(panelGroup1, BoxLayout.X_AXIS));
        panelGroup1.add(rangeView);

        buttonPanel = new ButtonPanel(this);

        panelGroup0 = new JPanel();
        panelGroup0.setLayout(new BoxLayout(panelGroup0, BoxLayout.Y_AXIS));
        panelGroup0.add(panelGroup1);
        panelGroup0.add(buttonPanel);

        add(panelGroup0);

        setScale(32);
        setLanderPos (0.0, 1.8);

        setSize(800, 500);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setFocusable(true);

        SoundEffect.init();
    }

    public void rcs_ccw() {
        rangeView.rcs_ccw();
    }
    public void rcs_cw() {
        rangeView.rcs_cw();
    }
    public void rcs_zero() {
        rangeView.rcs_zero();
    }
    public int get_rcs_state(){
        return rangeView.get_rcs_state();
    }
    public void throttleUp() {
        rangeView.throttleUp();
    }
    public void throttleDown() {
        rangeView.throttleDown();
    }

    public boolean getAuto_1() { return rangeView.getAuto_1(); };
    public void toggleAuto_1() { rangeView.toggleAuto_1(); };
    public boolean getAuto_2() { return rangeView.getAuto_2(); };
    public void toggleAuto_2() { rangeView.toggleAuto_2(); };

    public int getThrottleDelta() {
        return rangeView.getThrottleDelta();
    }
    public void setLanderAngle(double angle_r) {
        rangeView.setLanderAngle(angle_r);
    }
    public void setLanderAngleRate(double angle_rate) {
        rangeView.setLanderAngleRate(angle_rate);
    }
    public void setLanderPos(double x, double y) {
        rangeView.setLanderPos(x,y);
    }

    public void setLanderVel(double vx, double vy) {
        rangeView.setLanderVel(vx,vy);
    }

    public void setLanderThrottle(int percent) {
        rangeView.setLanderThrottle(percent);
    }

    public void setExplosionSize(double size) {
        rangeView.setExplosionSize(size);
    }

    public void setExplosionPos(double x, double y) {
        rangeView.setExplosionPos(x,y);
    }

    public void setScale(int value) {
        rangeView.setScale(value);
    }

    public int getScale() {
        return rangeView.getScale();
    }

    public void connectToServer(String host, int port ) throws IOException {
        Socket socket = new Socket(host, port);
        in = new BufferedReader( new InputStreamReader( socket.getInputStream()));
        out = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));
    }

    public void drawRangeView() {
        rangeView.repaint();
    }

    private static void  printHelpText() {
        System.out.println(
            "----------------------------------------------------------------------\n"
          + "usage: java jar LanderDisplay.jar <port-number>\n"
          + "----------------------------------------------------------------------\n"
          );
    }

    public enum ModelState { INACTIVE, READY, ACTIVE }

    public static void main(String[] args) throws IOException, InterruptedException {

        String host = "localHost";
        int port = 0;
        boolean boom = false;

        // ==========================================================
        // Handle program arguments.
        // ==========================================================
        int ii = 0;
        while (ii < args.length) {
            switch (args[ii]) {
                case "-help" :
                case "--help" : {
                    printHelpText();
                    System.exit(0);
                } break;
                default : {
                    port = (Integer.parseInt(args[ii]));
                } break;
            }
            ++ii;
        }

        boolean go = true;
        double dt = 0.100; // Time between updates (seconds).
        double posx = 0.0;
        double posy = 0.0;
        double angle = 0.0;
        double angle_rate = 0.0;
        double velx = 0.0;
        double vely = 0.0;
        int throttle = 0;

        // Outbound command variables
        int throttle_delta;
        int rcs_state;
        int Auto_1, Auto_2;

        boolean impact = false;
        boolean prevImpact = false;
        // boolean armCommand;
        // boolean fireCommand;
        int simMode = 0;
        boolean standalone = false;

        int     exticks = 0;
        double  exTime = 0.0;
        ModelState explosionModelState = ModelState.INACTIVE;

        int mapScale = 32 ; // pixels per meter.

        RangeView rangeView = new RangeView( mapScale);
        LanderDisplay evd = new LanderDisplay( rangeView);
        evd.setVisible(true);
        evd.drawRangeView();

if (!standalone) {
        if (port == 0) {
            System.out.println("No variable server port specified.");
            printHelpText();
            System.exit(0);
        }

        // Connect to the Trick simulation's variable server
        System.out.println("Connecting to: " + host + ":" + port);
        evd.connectToServer(host, port);

        evd.out.writeBytes("trick.var_set_client_tag(\"LanderDisplay\") \n");
        evd.out.flush();

        // Have the Variable Server send us the simulation mode ONCE.
        evd.out.writeBytes( "trick.var_add(\"trick_sys.sched.mode\")\n" +
                            "trick.var_send() \n" +
                            "trick.var_clear() \n");
        evd.out.flush();

        // Read the response and extract the simulation mode.
        try {
            String line;
            String field[];
            line = evd.in.readLine();
            field = line.split("\t");
            simMode = Integer.parseInt( field[1]);
        } catch (IOException | NullPointerException e ) {
            go = false;
        }

        // Configure the Variable Server to cyclically send us the following varibales.
        // Tell the variable server:
        //  1) We want the values of the following variables:
        evd.out.writeBytes( "trick.var_pause() \n" +
                            "trick.var_add(\"dyn.lander.pos[0]\")\n" +
                            "trick.var_add(\"dyn.lander.pos[1]\")\n" +
                            "trick.var_add(\"dyn.lander.angle\")\n" +
                            "trick.var_add(\"dyn.lander.vel[0]\")\n" +
                            "trick.var_add(\"dyn.lander.vel[1]\")\n" +
                            "trick.var_add(\"dyn.lander.angleDot\")\n" +
                            "trick.var_add(\"dyn.lander.throttle\")\n" +
                            "trick.var_add(\"trick_sys.sched.mode\")\n" +
        //  2) We want the responses in ASCII:
                            "trick.var_ascii() \n" +
        //  3) We want values to be updated at the specified rate:
                            String.format("trick.var_cycle(%.3f)\n", dt) +
        //  4) Start sending values as specified.
                            "trick.var_unpause() \n" );
        evd.out.flush();
    }


        while (go) {

if (!standalone) {

            // Recieve and parse periodic data response from the variable server.
            try {
                String line;
                String field[];
                line = evd.in.readLine();
                field = line.split("\t");
                posx   = Double.parseDouble( field[1]);
                posy   = Double.parseDouble( field[2]);
                angle  = Double.parseDouble( field[3]);
                velx   = Double.parseDouble( field[4]);
                vely   = Double.parseDouble( field[5]);
                angle_rate = Double.parseDouble( field[6]);
                throttle = Integer.parseInt( field[7]);
                simMode = Integer.parseInt( field[8]);
            } catch (IOException | NullPointerException e ) {
                go = false;
            }

            if (simMode == TrickSimMode.RUN) {
                if (boom) {
                    SoundEffect.CANNONBOOM.play();
                    boom = false;
                }
            }

            // Update the display data.
            evd.setLanderPos(posx, posy);
            evd.setLanderVel(velx, vely);
            evd.setLanderAngle(angle);
            evd.setLanderAngleRate(angle_rate);
            evd.setLanderThrottle(throttle);

            throttle_delta = rangeView.getThrottleDelta();
            evd.out.writeBytes( String.format("dyn.lander.manual_throttle_change_command = %d ;\n", throttle_delta ));
            rangeView.throttleZeroDelta();

            rcs_state = rangeView.get_rcs_state();
            evd.out.writeBytes( String.format("dyn.lander.manual_rcs_command = %d ;\n", rcs_state ));
            rangeView.rcs_zero();

            if (rangeView.getAuto_1()) Auto_1 = 1; else Auto_1 = 0;
            evd.out.writeBytes( String.format("dyn.lander.Auto_1 = %d ;\n", Auto_1 ));

            if (rangeView.getAuto_2()) Auto_2 = 1; else Auto_2 = 0;
            evd.out.writeBytes( String.format("dyn.lander.Auto_2 = %d ;\n", Auto_2 ));

            evd.out.flush();

            // Explosion Model
            exticks ++;
            exTime = exticks * dt;
            switch(explosionModelState) {
                case INACTIVE:
                    if (impact && !prevImpact) { // Trigger on leading edge.
                        exticks = 0;
                        evd.setExplosionPos(posx, posy);
                        explosionModelState = ModelState.ACTIVE;
                        SoundEffect.EXPLOSION.play();
                    }
                    break;
                case ACTIVE:
                    if (exTime > 4.0) {
                        evd.setExplosionSize(0.0);
                        explosionModelState = ModelState.INACTIVE;
                    } else if (exTime > 0.0) {
                        evd.setExplosionSize(exTime * exTime * 5.0);
                    } else {
                        evd.setExplosionSize(0.0);
                    }
                    break;
                default:
                    break;
            }
            prevImpact = impact;
}
            //  Update the scene.
            evd.drawRangeView();

        } // while
    } // main
} // class

