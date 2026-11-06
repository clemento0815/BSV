% Darstellen der Punktkinematik für das Schreiben eines Undendlich-Symbols

% (1) laden der Daten (Spaltentrennsymbol "," und 2 Header-lines)
m = importdata("data.txt",",",2);
Nend = 620;  
Nstart = 10;
indData = Nstart:Nend;
t = m.data(indData, 1); % 1. Spalte
x = m.data(indData, 2); % 2. Spalte
y = m.data(indData, 3); % 3. Spalte

% (2) Filtern der Koordinaten
wlen = 101;  % Fenstergroesse für den Filter (mehr glätten, wenn gross
order = 3;   % Ordnung des Filters
xf = sgolayfilt(x, order, wlen); % Savitzky-Golay Filter
yf = sgolayfilt(y, order, wlen);


% (3) Koordinaten plotten (Vergleich mit Filterung)
figure(1);
clf;
plot(t, x, 'r:', "DisplayName", "Messdaten x"); hold on;
plot(t, xf, 'r-', "DisplayName", "Gefiltert x"); hold on;
plot(t, y, 'b:', "DisplayName", "Messdaten y"); hold on;
plot(t, yf, 'b-', "DisplayName", "Gefiltert y"); hold off;
grid on;
xlabel("x (m)");
ylabel("y (m)");
title("x-y Koordinaten")
legend()


% (4) Ableiten nach der Zeit (mumerisch)
deltat = mean(diff(t));
vx = [0; diff(xf)]/deltat;
vy = [0; diff(yf)]/deltat;
ax = [0; diff(vx)]/deltat;
ay = [0; diff(vy)]/deltat;

% (5) Geschw. und Beschl. plotten
figure(2);
clf;
ind = 1:15:length(xf); % nur jeden 15. Wert den Vektor zeichnen
qpv = quiver(xf(ind), yf(ind), vx(ind), vy(ind), 'g', "DisplayName", "v"); hold on;
qpv.MaxHeadSize = 0.05; 
qpa = quiver(xf(ind), yf(ind), ax(ind), ay(ind), 'm', "DisplayName", "a"); hold on;
qpa.MaxHeadSize = 0.05;

% beschleunigte bzw. verzoegerte Bereiche
ind_beschl = find(vx.*ax + vy.*ay >= 0);
ind_verz = find(vx.*ax + vy.*ay < 0);

plot(xf(ind_beschl), yf(ind_beschl), 'r.', "DisplayName", "beschleunigt"); hold on;
plot(xf(ind_verz), yf(ind_verz), 'b.', "DisplayName", "verzoegert"); hold on;
plot(xf(ind), yf(ind), 'co', "MarkerFaceColor", "c", ...
    "MarkerSize", 3, "DisplayName", "ausgew. Punkte"); hold on;
hold off;
grid on;
xlabel("x (m)");
ylabel("y (m)");
title("Momentangeschwindigkeit und -beschleunigung")
legend();