m = 1000;
b = 50;
u = 500;

s = tf('s');
P_cruise = 1/(m*s+b);

Ts = 1/50;

dP_cruise = c2d(P_cruise,Ts,'zoh')

Wn = 0.0072;
zeta = 0.6;

rlocus(dP_cruise)
zgrid(zeta, Wn)
axis ([-1 1 -1 1])