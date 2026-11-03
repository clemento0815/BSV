%% numerische Lösung Feder-Masse-Dämpfer System
clear all
% Parameter
m=1;
c=10;
d=1;
F0 = 10;
t0 = 1;
tend = 15;

% Anfangsbedigungen
x0 = 0;
v0 = 0;

% Schrittweite

h = 1E-2;
N = ceil(tend/h);


% System = Kraft F
F = ones(1, N)*F0;
F(1:ceil(t0/h)) = 0;

% Iteration nach Euler
x(1) = x0;
v(1) = v0;

for i = 1:N-1
    x(i+1) = x(i) + h*v(i);
    v(i+1) = v(i) + h*(F(i) - c*x(i) - d*v(i))/m;
end

% Ergebnisse plotten

t=0:h:(N-1)*h;
figure(1);
clf;
yyaxis left;
plot(t,x);
yyaxis right;
plot(t,F, LineWidth=2);
xlabel(" t(s) ");
ylabel(" x(t) ");
grid on;