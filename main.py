import numpy as np
import matplotlib.pyplot as plt


def newton_raphson(x0, f, df):
    roots = np.copy(x0)  # lager nye arrays som funksjonen skal returnere
    steps = np.zeros(len(x0))  # array som skal lagre antall steg som krevdes for å finne røttene

    error_margin = 10 ** -12
    max_steps = 100

    for i in range(len(x0)):  # nested loop som går gjennom alle x0 verdiene
        for j in range(0, max_steps):  # loop for å prøve å finne rota for x0

            if df(x0[i]) == 0:  # sjekker om den deriverte er 0 så vi ikke får et udefinert uttrykk
                print('Undefined')
                break

            x1 = roots[i] - f(roots[i]) / df(roots[i])  # selve newton-raphson metoden
            roots[i] = x1  # oppdaterer x-verdien for neste iterasjon

            if j > max_steps:  # sjekker om vi har gått over max antall forsøk vi har bestemt
                steps[i] = None
                roots[i] = None
                print('No roots found')
                break
            if not 10*x0[0] < x1 < 10*x0[-1]:  # luker ut gjetninger som går langt utenfor området
                roots[i] = None
                steps[i] = None
                break

            if abs(f(x1)) < error_margin:  # sjekker om vi er nærme nok rota i forhold til feilmarginen vi har satt
                steps[i] = j  # lagrer antall steg vi brukte for å finne rota
                break

    return roots, steps


def plot(x0, f, df):
    roots, steps = newton_raphson(x0, f, df)
    fig, axs = plt.subplots(2)
    fig.suptitle('x from {:.2f} to {:.2f} with {:.2f} points'.format(x0[0], x0[-1], len(x0)))

    axs[0].plot(x0, f(x0), x0, df(x0))
    axs[0].legend(['f(x)', "f'(x)"])
    axs[0].grid(True)
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("y")

    axs[1].plot(x0, roots, x0, steps)
    axs[1].legend(['roots', 'steps'])
    axs[1].grid(True)
    axs[1].set_xlabel("x0")
    axs[1].set_ylabel("x")

    axs2 = axs[1].twinx()
    axs2.plot(x0, roots, x0, steps)
    axs2.set_ylabel("number of steps")
    print_roots(roots)
    plt.show()


def print_roots(roots):
    np.round_(roots, decimals=6, out=roots)                # runder av røttene til 6 desimaler så det er lettere å se
    values, counts = np.unique(roots, return_counts=True)  # hvilke som egentlig er like, og finner ut hvor mange ganger
    ind = np.argpartition(-counts, kth=2)[:2]              # hver verdi dukker opp, printer ut de to røttene som
    print('\nRoots found:')                                # dukker opp flest ganger
    for i in ind:
        print('x = {} found from {} initial values'.format(values[i], counts[i]))
    print('Out of a total of {} initial values evaluated, {} failed'.format(len(roots), len(roots)-counts[ind[0]]-counts[ind[1]]))


# oppgave 1
def func_1(x):
    return 3 * x ** 2 + 4 * x - 4


def dfunc_1(x):
    return 6 * x + 4


# regner ut med forskjellige intervaller av x0-verdier for å studere oppførselen til metoden
plot(np.linspace(-1, 1, 100), func_1, dfunc_1)
plot(np.linspace(-5, 5, 100), func_1, dfunc_1)


# oppgave 2
def func_2(x):
    return 34*np.cos(theta_1-x)-40*np.cos(theta_1)-170*np.cos(x)-24*np.sin(theta_1)-102*np.sin(x) + 163.25


def dfunc_2(x):
    return -34*np.sin(x-theta_1)+170*np.sin(x)-102*np.cos(x)


# plotter de forskjellige theta_1 verdiene, med samme intervall fordi denne funksjonen er periodevis og vi er kun
# interessert i det som skjer innenfor samme periode

theta_1 = 0
plot(np.linspace(-np.pi, np.pi, 100), func_2, dfunc_2)

theta_1 = np.pi/2
plot(np.linspace(-np.pi, np.pi, 100), func_2, dfunc_2)

theta_1 = np.pi
plot(np.linspace(-np.pi, np.pi, 100), func_2, dfunc_2)