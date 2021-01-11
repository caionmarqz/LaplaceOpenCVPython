import sys
import cv2 as cv


def main(argv):
    depth = cv.CV_16S
    kernel_size = 3
    window_name = "Demonstração da tranformada de Laplace"
    imageName = argv[0] if len(argv) > 0 else 'lena.jpg'
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)
    if src is None:
        print('Erro ao abrir o arquivo')
        print('python3 laplace.py image_file_name.jpg')
        return -1
    # remoção de ruido
    src = cv.GaussianBlur(src, (3, 3), 0)
    # converter para cinza
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    # função de laplace
    dst = cv.Laplacian(src_gray, depth, ksize=kernel_size)
    # converter de volta ao formato inicial
    abs_dst = cv.convertScaleAbs(dst);
    cv.imshow(window_name, abs_dst)
    cv.waitKey(0)
    # [display]
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])
