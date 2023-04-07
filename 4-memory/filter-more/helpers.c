#include <math.h>

#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int average = ((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width / 2; j++)
        {

            int tempRed = image[i][(width - 1) - j].rgbtRed;
            image[i][(width - 1) - j].rgbtRed = image[i][j].rgbtRed;
            image[i][j].rgbtRed = tempRed;

            int tempGreen = image[i][(width - 1) - j].rgbtGreen;
            image[i][(width - 1) - j].rgbtGreen = image[i][j].rgbtGreen;
            image[i][j].rgbtGreen = tempGreen;

            int tempBlue = image[i][(width - 1) - j].rgbtBlue;
            image[i][(width - 1) - j].rgbtBlue = image[i][j].rgbtBlue;
            image[i][j].rgbtBlue = tempBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int counter = 0;
            int sumRed = 0, sumGreen = 0, sumBlue = 0;
            int aveRed, aveGreen, aveBlue;

            for(int x = -1; x < 2; x++)
            {
                for(int y = -1; y < 2; y++)
                {
                    if(i + x >= 0 && j + y >= 0 && i + x <= height && j + y <= width)
                    {
                        sumRed += temp[i + x][j + y].rgbtRed;
                        sumGreen += temp[i + x][j + y].rgbtGreen;
                        sumBlue += temp[i + x][j + y].rgbtBlue;

                        counter++;
                    }
                }
            }

            aveRed = sumRed / counter;
            aveGreen = sumGreen / counter;
            aveBlue = sumBlue / counter;

            image[i][j].rgbtRed = aveRed;
            image[i][j].rgbtGreen = aveGreen;
            image[i][j].rgbtBlue = aveBlue;
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    // Define the factor in 2D array and use multiplication of array and array to simplify the problem. Instead of putting in 6+6 different "if" conditions.
    int sobel_x[3][3] = {{-1, 0, 1,}, {-2, 0, 2,}, {-1, 0, 1,}};
    int sobel_y[3][3] = {{-1, -2, -1,}, {0, 0, 0,}, {1, 2, 1,}};

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {

            double GxRed = 0, GxGreen = 0, GxBlue = 0, GyRed = 0, GyGreen = 0, GyBlue = 0;

            for(int x = -1; x < 2; x++)
            {
                for(int y = -1; y < 2; y++)
                {
                    if(i + x < 0 || j + y < 0 || i + x > height || j + y > width)
                    {
                        continue;
                    }
                    else
                    {
                        GxRed += (temp[i + x][j + y].rgbtRed) * (sobel_x[x + 1][y + 1]);
                        GxGreen += (temp[i + x][j + y].rgbtGreen) * (sobel_x[x + 1][y + 1]);
                        GxBlue += (temp[i + x][j + y].rgbtBlue) * (sobel_x[x + 1][y + 1]);

                        GyRed += (temp[i + x][j + y].rgbtRed) * (sobel_y[x + 1][y + 1]);
                        GyGreen += (temp[i + x][j + y].rgbtGreen) * (sobel_y[x + 1][y + 1]);
                        GyBlue += (temp[i + x][j + y].rgbtBlue) * (sobel_y[x + 1][y + 1]);
                    }
                }
            }

            int red = round(sqrt((GxRed * GxRed) + (GyRed * GyRed)));
            int green = round(sqrt((GxGreen * GxGreen) + (GyGreen * GyGreen)));
            int blue = round(sqrt((GxBlue * GxBlue) + (GyBlue * GyBlue)));

            if(red > 255)
            {
                red = 255;
            }

            if(green > 255)
            {
                green = 255;
            }

            if(blue > 255)
            {
                blue = 255;
            }

            image[i][j].rgbtRed = red;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtBlue = blue;
        }
    }
    return;
}

void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed, sepiaGreen, sepiaBlue;

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;

            if(sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            if(sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            if(sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }

            image[i][j].rgbtRed = round(sepiaRed);
            image[i][j].rgbtGreen = round(sepiaGreen);
            image[i][j].rgbtBlue = round(sepiaBlue);
        }
    }

    return;
}