m = 1000;
b = 50;
u = 500;

Kp = 1;
s = tf('s');
P_cruise = 1/(m*s+b);
C = Kp;
r = 10;
sys_cl = feedback(C*P_cruise,1);
bode(C*P_cruise);