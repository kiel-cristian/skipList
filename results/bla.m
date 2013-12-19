insertn10abbr = [15.6447 16.1345 15.4597 15.7311 16.1646 16.8287 15.7988 15.6777 15.8483 17.3535];
insertn10sl = [9.9449 10.9881 10.1737 10.4188 10.8715 11.2728 13.7768 10.8205 11.0062 10.6027];
search10abbr = [15.5762 17.0402 15.3694 15.9116 17.8072 16.521 17.4944 15.8522 15.9794 15.659];
search10sl = [10.5938 12.4832 10.6316 11.0728 11.0542 12.6316 13.9548 12.1532 11.8564 12.168];

insertn20abbr = [17.15155 18.0494 17.35815 17.68725 17.6777 18.32485 17.8953 17.8953 16.8175 17.3304 18.84055];
insertn20sl = [12.8931 11.4958 11.78085 12.95175 12.0059 12.57445 11.96915 13.56575 12.9497 12.32685];

X = [10000 20000 50000];
x = 0:100:60000;
logX = log(X);
iABBRY = [16.06416 17.71326 19.59822];
iSLY = [10.9876 12.45133 13.597384];
sABBRY = [16.32106 18.06532 19.850128];
sSLY = [11.85996 13.25466 14.583764];

c = polyfit(logX,iABBRY,1)
c = polyfit(logX,iSLY,1)
c = polyfit(logX,sABBRY,1)
c = polyfit(logX,sSLY,1)

#{
c = polyfit(logX,iABBRY,1)
f = c(2).+c(1).*log(x);
hold on;
axis([0 60000 0 25]);
plot(X, iABBRY, '-or');
plot(x, f);
xlabel ("Número de inserciones");
ylabel ("Promedio de comparaciones por inserción");
print -dsvg iABBR.svg
hold off; clearplot;

c = polyfit(logX,iSLY,1)
f = c(2).+c(1).*log(x);
hold on;
axis([0 60000 0 25]);
plot(X, iSLY, '-or');
plot(x, f);
xlabel ("Número de inserciones");
ylabel ("Promedio de comparaciones por inserción");
print -dsvg iSL.svg
hold off; clearplot;
#}
c = polyfit(logX,sABBRY,1)
f = c(2).+c(1).*log(x);
hold on;
axis([0 60000 0 25]);
plot(X, sABBRY, '-or');
plot(x, f);
xlabel ("Número de búsquedas");
ylabel ("Promedio de comparaciones por búsqueda");
print -dsvg sABBR.svg
hold off; clearplot;
#{
c = polyfit(logX,sSLY,1)
f = c(2).+c(1).*log(x);
hold on;
axis([0 60000 0 25]);
plot(X, sSLY, '-or');
plot(x, f);
xlabel ("Número de búsquedas");
ylabel ("Promedio de comparaciones por búsqueda");
print -dsvg sSL.svg
hold off; clearplot;
#}
