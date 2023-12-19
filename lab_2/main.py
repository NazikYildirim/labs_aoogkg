import matplotlib.pyplot as plt

# Reading file (dataset) and returning 2 lists with coordinates x and y
def read_file(file_path):
    x_coordinate, y_coordinate = [], []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            x_coordinate.append(x)
            y_coordinate.append(y)
    return x_coordinate, y_coordinate

# Displaying points on the canvas 960x540 px
def display_points(x_coordinate, y_coordinate):
    plt.figure(figsize=(960/80, 540/80))
    plt.scatter(x_coordinate, y_coordinate, color='purple', marker='o')
    plt.title('Result')
    plt.xlabel('x', fontsize = 18)
    plt.ylabel('y', fontsize = 18)
    plt.show()

# Saving the result in PNG format
def save_result(x_coordinate, y_coordinate, result):
    plt.figure(figsize=(960/80, 540/80))
    plt.scatter(x_coordinate, y_coordinate, color='purple', marker='o')
    plt.title('Result')
    plt.xlabel('x', fontsize = 18)
    plt.ylabel('y', fontsize = 18)
    plt.savefig(result, format='png')

if __name__ == "__main__":
    dataset_file = "DS1.txt"
    result = "result.png"

    x_coordinate, y_coordinate = read_file(dataset_file)
    display_points(x_coordinate, y_coordinate)
    save_result(x_coordinate, y_coordinate, result)