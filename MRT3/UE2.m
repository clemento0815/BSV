% Autor: Clemens Loher
% Date: 03.11.2026

% Programmieren der Temperaturkennlinie von PTC und NTC Thermistoren
clc
clear all

%% Teil 1

% Koeffizienten definieren
R0PTC00 = 500;
alpha = 3.90802e-3;
beta = -5.802e-7;
Temperatur1 = [0:0.01:100]; % Temperaturbereich von 0 °C - 100 °C
Temperatur2 = [0:0.01:1200]; % Temperaturbereich von 0 °C - 1200 °C

% Formeln
Widerstand1 = R0PTC00 .* (1 + alpha .* Temperatur1 + beta .* Temperatur1.^2);
Widerstand2 = R0PTC00 .* (1 + alpha .* Temperatur2 + beta .* Temperatur2.^2);
Widerstandohnebeta = R0PTC00 .* (1 + alpha .* Temperatur2);

% Temperaturkennlinie des PTC
figure(1)
plot(Temperatur1, Widerstand1, 'r')
grid on
xlabel("Temperatur[°C]")
ylabel("Widerstand [Ohm]")
title("Temperaturkennlinie des PTC-Thermistors")
legend("PTC")

figure(2)
plot(Temperatur2, Widerstand2, 'r')
grid on
xlabel("Temperatur[°C]")
ylabel("Widerstand [Ohm]")
title("Temperaturkennlinie des PTC-Thermistors")
legend("PTC")

figure(3)
plot(Temperatur2, Widerstand2, 'g')
hold on
plot(Temperatur2, Widerstandohnebeta, 'r--')
xlabel("Temperatur[°C]")
ylabel("Widerstand [Ohm]")
hold off
legend('Widersta mit beta','Widerstand ohne beta')
title("Temperaturkennlinie des PTC-Thermistors")

%% Teil 2

% Koeffizienten
T0 = 20
R0NTC20 = 20000; %  Widerstand R0 von 20000 Ohm bei 20 °C
B = 3000; % Materialparameter


% Formel
RT = R0NTC20 .* exp(B .* (1./(Temperatur1 + 273.15) - 1./(T0 + 273.15)));

% Temperaturkennlinie des NTC darstellen
figure(4)
plot(Temperatur1, RT, 'b')
grid on
xlabel("Temperatur [°C]")
ylabel("Widerstand [Ohm]")
title("Temperaturkennlinie des NTC-Thermistors")
legend("NTC")


