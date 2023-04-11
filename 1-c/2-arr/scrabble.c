#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet: a or A is points[0]......
int POINTS[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    if(score1 > score2)
    {
        printf("Player 1 wins\n");
    }
    else
    {
        if(score2 > score1)
        {
        printf("Player 2 wins\n");
        }
        else
        {
            printf("Tie\n");
        }
    }
}

int compute_score(string word)
{
    int i;

    int score = 0;

    int n = strlen(word);
    // Upper case ASCII value range from 65 to 90 while lower case range from 97 to 122
    for(i = 0; i < n; i++)
    {
        word[i] = toupper(word[i]);
    }

    for(i = 0; i < n; i++)
    {
        if(word[i] >= 65 && word[i] <= 90)
        {
        score += POINTS[word[i] - 65];
        }
        else
        {
            score += 0;
        }
    }

    return score;
}
