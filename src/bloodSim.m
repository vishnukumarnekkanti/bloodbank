clear all;
x = [0:0.1:3650];
y = 0.5*(cos(x) - cos(2*x) - cos(3*x));
noisy_y = 1 + abs(y+0.2*rand(1, length(y)));
#plot(x,noisy_y)
file_id = fopen('input.txt', 'w');
for i = [1:3650]
    fprintf(file_id,'%d,%u\n',i,noisy_y(i));
endfor
