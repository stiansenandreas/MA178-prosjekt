import numpy as np
import matplotlib.pyplot as plt


def newton_raphson(x0, f, df):
    roots = np.copy(x0)  # lager nye arrays som funksjonen skal returnere
    steps = np.zeros(len(x0))  # array som skal lagre antall steg som krevdes for å finne røttene

    error_margin = 10 ** -12
    max_steps = 100

    for i in range(len(x0)):  # nested loop som går gjennom alle x0 verdiene

        if df(x0[i]) == 0:  # sjekker om den deriverte er 0 så vi ikke får et udefinert uttrykk
            roots[i] = None
            steps[i] = None
            continue

        for j in range(0, max_steps):  # loop for å prøve å finne en rot med x0

            roots[i] += - f(roots[i]) / df(roots[i])  # selve newton-raphson metoden

            if j > max_steps or not 10 * x0[0] < roots[i] < 10 * x0[-1]:  # sjekker om vi har gått over max antall
                steps[i] = None                                           # forsøk, og luker også ut gjetninger som går
                roots[i] = None                                           # langt utenfor området, funker fint så lenge
                break                                                     # intervallet er symmetrisk om y-aksen

            if abs(f(roots[i])) < error_margin:  # sjekker om vi er nærme nok rota i forhold til marginen vi har satt
                steps[i] = j                     # lagrer antall steg vi brukte for å finne rota
                break

    return roots, steps


def print_roots(roots):
    np.round_(roots, decimals=6, out=roots)                # runder av røttene til 6 desimaler så det er lettere å se
    values, counts = np.unique(roots, return_counts=True)  # hvilke som egentlig er like, og finner ut hvor mange ganger
    ind = np.argpartition(-counts, kth=2)[:2]              # hver verdi dukker opp, printer ut de to verdiene som
    print('\nRoots found:')                                # dukker opp flest ganger

    for i in ind:
        if assignment == 1:
            print('x = {} evaluated from {} initial values'.format(values[i], counts[i]))
        elif assignment == 2:
            print('x= {} evaluated from {} initial values, {:.2f} radians is {:.2f} degrees'.format(
                values[i], counts[i], values[i], values[i]*(180/np.pi)))     # konverter også til grader for oppgave 2

    print('Out of a total of {} initial values evaluated, {} failed'.format(
        len(roots), len(roots) - counts[ind[0]] - counts[ind[1]]))

    return [values[i] for i in ind]


def plot(x0, f, df):
    roots, steps = newton_raphson(x0, f, df)
    root_values = print_roots(roots)

    for i in range(len(root_values)):               # lager ikke et punkt for rota i grafen hvis den ikke er
        if not x0[0] < root_values[i] < x0[-1]:     # innenfor intervallet vi ser på
            del root_values[i]

    fig, axs = plt.subplots(2)

    if assignment == 1:   # overskrifter til grafene
        fig.suptitle('x from {} to {} with {} points'.format(x0[0], x0[-1], len(x0)))
    elif assignment == 2:
        fig.suptitle(
            'x from {:.2f} to {:.2f} with {} points, and theta_1 = {:.2f}'.format(x0[0], x0[-1], len(x0), theta_1))

    axs[0].plot(x0, f(x0), x0, df(x0))   # øverste grafen med funksjonene f og df og punkter på røttene
    axs[0].legend(['f(x)', "f'(x)"])
    axs[0].grid(True)
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("y")
    axs[0].plot([i for i in root_values], np.zeros(len(root_values)), ls='', marker='o', c='r')  # punkter for røttene
    for x, y in zip(root_values, np.zeros(len(root_values))):
        axs[0].annotate('x = {:.3f}'.format(x), xy=(x, y), textcoords='data')

    axs[1].plot(x0, roots, x0, steps)   # nederste grafen med en oversikt over røtter for hver x0 samt antall steg
    axs[1].legend(['roots', 'steps'])
    axs[1].grid(True)
    axs[1].set_xlabel("x0")
    axs[1].set_ylabel("x")

    axs_2 = axs[1].twinx()                   # kloner og speiler den nederste grafen slik at vi kan ha en label for
    axs_2.set_ylabel("number of steps")      # hver side av y-aksen

    plt.show()


assignment = 1


def func_1(x):
    return 3 * x ** 2 + 4 * x - 4


def dfunc_1(x):
    return 6 * x + 4


# regner ut med forskjellige intervaller av x0-verdier for å studere oppførselen til metoden

plot(np.linspace(-1, 1, 1000), func_1, dfunc_1)
plot(np.linspace(-5, 5, 1000), func_1, dfunc_1)


assignment = 2


def func_2(x):
    return (34 * np.cos(theta_1 - x) - 40 * np.cos(theta_1) - 170 * np.cos(x) - 24 * np.sin(theta_1)
            - 102 * np.sin(x) + 163.25)


def dfunc_2(x):
    return -34 * np.sin(x - theta_1) + 170 * np.sin(x) - 102 * np.cos(x)


# plotter de forskjellige theta_1 verdiene, med de to samme intervallene fordi denne funksjonen er periodevis og vi er
# kun interessert i de to røttene som er innenfor samme periode

theta_1 = 0
plot(np.linspace(-np.pi, np.pi, 100), func_2, dfunc_2)

theta_1 = np.pi / 2
plot(np.linspace(-np.pi, np.pi, 100), func_2, dfunc_2)

theta_1 = np.pi
plot(np.linspace(-np.pi, np.pi, 100), func_2, dfunc_2)