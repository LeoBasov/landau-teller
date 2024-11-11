def write_solution(solution, file_name, format):
    if format == 'csv':
        write_solution_csv(solution, file_name)
    else:
        raise Exception("undefined format [" + format + "]")
    
def write_solution_csv(solution, file_name):
    with open(file_name + "_temp.csv", "w") as file:
        file.write("t, temp, trot")

        for i in range(solution.temperatures[0].size - 2):
            file.write(", tvib_" + str(i + 1))

        file.write("\n")

        for i in range(len(solution.time)):
            file.write(str(solution.time[i]))

            for temp in solution.temperatures[i]:
                file.write(", " + str(temp))

            file.write("\n")

    with open(file_name + "_energy.csv", "w") as file:
        file.write("t, ekin, erot")

        for i in range(solution.temperatures[0].size - 2):
            file.write(", evib_" + str(i + 1))

        file.write("\n")

        for i in range(len(solution.time)):
            file.write(str(solution.time[i]))

            for energy in solution.energies[i]:
                file.write(", " + str(energy))

            file.write("\n")