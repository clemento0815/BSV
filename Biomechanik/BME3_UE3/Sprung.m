% Sprung
clear all;
load ("Jump_roedi_03.mat");

Fz = forceplateData.Fz;
t = seconds(forceplateData.Time);
t = t - t(1);



% Impuls
% die erste Sekunde = Stehen
t_stehen = 0.1;
ind_Stehen = find(t <= t_stehen);
Fg = mean(Fz(ind_Stehen));
% dynamischer Kraftanteil
Fdyn = Fz-Fg;
Jz = cumtrapz(t, Fdyn);

% Plotten
figure(1);
yyaxis left;
plot(t,Fz,LineWidth=2);
grid on;
xlabel("t (s)");
ylabel("Fz (N)");

yyaxis right;
plot(t, Jz);
ylabel("Jz (Ns)")