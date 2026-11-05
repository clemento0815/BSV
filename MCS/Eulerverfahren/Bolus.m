function [] = Bolus()
%% Modell des i.v. Bolus
par.D = 1000;
par.k12 = 0.6;
par.k21 = 1.25;
par.k10 = 0.2;

% Schrittweite
tend = 24; % entspricht 24 Stunden, alle Austauschraten sind in Stunden 

% Aufrufen der Funktion
h1 = 0.01;
[t1, Xp1, Xc1, E1] = bolus_euler_iteration(tend, h1, par);

h2 = 0.4;
[t2, Xp2, Xc2, E2] = bolus_euler_iteration(tend, h2, par);

% plotten
figure(1);
clf; % Grafikfenster vorher leeren

% h1 (Schrittweite 0.01) als durchgezogene Linien
plot(t1, Xc1, 'b', t1, Xp1, 'r', t1, E1, 'y', 'LineWidth', 1.5); 
hold on; % <--- WICHTIG: Erlaubt das Zeichnen mehrerer Graphen in ein Diagramm!

% h2 (Schrittweite 0.1) als gestrichelte Linien
plot(t2, Xc2, 'b--', t2, Xp2, 'r--', t2, E2, 'y--', 'LineWidth', 1.5);

xlabel('Zeit (h)');
ylabel('Stoffmenge');
legend('Zentral (h=0.01)', 'Peripher (h=0.01)', 'Eliminiert (h=0.01)', ...
       'Zentral (h=0.1)', 'Peripher (h=0.1)', 'Eliminiert (h=0.1)', 'Location', 'best');
grid on;
hold off;
end

function [t, Xp, Xc, E] = bolus_euler_iteration(tend, h, par)
% Parameter 
D = par.D;
k12 = par.k12;
k21 = par.k21;
k10 = par.k10;

% Anfangsbedingungen
Xc(1) = D;
Xp(1) = 0;
E(1)  = 0;

N = ceil(tend/h);

% Iteration nach Euler
for i = 1:N-1
    Xc(i+1) = Xc(i) + h*(-k12*Xc(i) + k21*Xp(i) - k10*Xc(i));
    Xp(i+1) = Xp(i) + h*(-k21*Xp(i) + k12*Xc(i));
    E(i+1)  = E(i)  + h*k10*Xc(i);
end

% Zeitvektor
t = 0:h:(N-1)*h;
end