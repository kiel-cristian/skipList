function swap_curve
    load ADJUST10000;
    n = 10000;
    d_swap = 0.05*n;

    abb   = ADJUST10000(:,1)
    abb_r = ADJUST10000(:, 2)
    skip  = ADJUST10000(:, 3)
    len = 15;

    swaps = d_swap:d_swap:d_swap*len;

    hold on;
    plot(swaps, abb, swaps, abb_r, swaps, skip);
    legend('ABB', 'ABB aleatorizado', 'SkipList');
    # errorbar(x, m, s);

    axis([500 len*500 0 70]);
    xlabel ("Cantidad de swaps");
    ylabel ("Comparaciones de claves");
    title('Curva de ajuste de comparaciones N = 10000');
    print -dsvg swaps.svg;
endfunction

function global_swap
    SWAPS = [7000, 15700, 36500]
    ERROR = [8276.47267862, 13118.6889589, 31264.9964017]
    n     = [10000, 20000, 50000]

    hold off;
    bar(n, SWAPS);
    errorbar(n, SWAPS, ERROR);
    # legend('Swaps');

    axis([0 60000 -10000 70000]);
    xlabel ("Cantidad de elementos (N)");
    ylabel ("Cantidad de swaps (k)");
    title('Curva de swaps en función de N');
    print -dsvg global_swaps.svg;
endfunction

swap_curve()
global_swap()