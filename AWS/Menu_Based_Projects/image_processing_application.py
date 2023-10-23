from PIL import Image

# Function to open and display an image
def open_image():
    image_path = input("Enter the path of the image file: ")
    try:
        image = Image.open(image_path)
        image.show()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to resize an image
def resize_image():
    image_path = input("Enter the path of the image file to resize: ")
    try:
        image = Image.open(image_path)
        width = int(input("Enter the new width: "))
        height = int(input("Enter the new height: "))
        resized_image = image.resize((width, height))
        resized_image.show()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to apply grayscale to an image
def grayscale_image():
    image_path = input("Enter the path of the image file to convert to grayscale: ")
    try:
        image = Image.open(image_path)
        grayscale_image = image.convert("L")
        grayscale_image.show()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to apply rotation to an image
def rotate_image():
    image_path = input("Enter the path of the image file to rotate: ")
    try:
        image = Image.open(image_path)
        angle = int(input("Enter the rotation angle (in degrees): "))
        rotated_image = image.rotate(angle)
        rotated_image.show()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to display the menu and handle user choices
def main():
    while True:
        print("\nImage Processing Menu:")
        print("1. Open and Display Image")
        print("2. Resize Image")
        print("3. Convert Image to Grayscale")
        print("4. Rotate Image")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            open_image()
        elif choice == '2':
            resize_image()
        elif choice == '3':
            grayscale_image()
        elif choice == '4':
            rotate_image()
        elif choice == '5':
            print("Exiting Image Processing Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
