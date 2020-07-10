def tower_of_hanoi(n, src_pole, des_pole, temp_pole):
    if n == 1:
        print(f"Move disk 1 from rod {src_pole} to rod {des_pole}")
        return

    tower_of_hanoi(n-1, src_pole, temp_pole, des_pole)
    print(f"Move disk {n} from rod {src_pole} to rod {des_pole}")
    tower_of_hanoi(n-1, temp_pole, des_pole, src_pole)


#driver program
tower_of_hanoi(3, 'A', 'C', 'B')