from lab_13 import *

if __name__ == "__main__":
    f = lambda x: ((x**4) - (3*x**3) + (2*x) - 6)
    
    output_b = open('метод бісекції.txt', 'w')
    output_b.write("Корінь №1\n\n")
    B1 = Polynom(f, -1.26, -0.557507, 0.00001, 'b', output_b)
    output_b.write("\nf({})=0; Кількість ітерацій дорівнює {};\nЧас виконання дорівнює {} c\n".format(B1.root, B1.iterations, B1.duration))
    output_b.write("\n\\----------------------------------------------\\\n")
    output_b.write("\nКорінь №2\n\n")
    B2 = Polynom(f, 0.75, 3.2, 0.00001, 'b', output_b)
    output_b.write("\nf({})=0; Кількість ітерацій дорівнює {};\nЧас виконання дорівнює {} c".format(B2.root, B2.iterations, B2.duration))
    output_b.close()

    output_c = open('метод хорд.txt', 'w')
    output_c.write("Корінь №1\n\n")
    C1 = Polynom(f, -1.26, -0.557507, 0.00001, 'c', output_c)
    output_c.write("\nf({})=0; Кількість ітерацій дорівнює {};\nЧас виконання дорівнює {} c\n".format(C1.root, C1.iterations, C1.duration))
    output_c.write("\n\\----------------------------------------------\\\n")
    output_c.write("\nКорінь №2\n\n")
    C2 = Polynom(f, 0.75, 3.2, 0.00001, 'c', output_c)
    output_c.write("\nf({})=0; Кількість ітерацій дорівнює {};\nЧас виконання дорівнює {} c".format(C2.root, C2.iterations, C2.duration))
    output_c.close()

    output_t = open('метод дотичних.txt', 'w')
    output_t.write("Корінь №1\n\n")
    T1 = Polynom(f, -1.26, -0.557507, 0.00001, 'c', output_t)
    output_t.write("\nf({})=0; Кількість ітерацій дорівнює {};\nЧас виконання дорівнює {} c\n".format(T1.root, T1.iterations, T1.duration))
    output_t.write("\n\\----------------------------------------------\\\n")
    output_t.write("\nКорінь №2\n\n")
    T2 = Polynom(f, 0.75, 3.2, 0.00001, 'c', output_t)
    output_t.write("\nf({})=0; Кількість ітерацій дорівнює {};\nЧас виконання дорівнює {} c".format(T2.root, T2.iterations, T2.duration))
    output_t.close()