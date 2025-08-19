m = 1000;
b= 50;
r = 10 ;

s=tf('s');
P_cruise = 1/(m*s + b);

zo = 0.3;
po = 0.03;

s = tf('s');
C_lag = (s+zo)/(s+po);




Kp = 1293.6;
sys_cl = feedback(Kp*C_lag*P_cruise,1);
t = 0:0.1:20;
step(r*sys_cl,t)
axis([0 20 0 12])