#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser represented in candidate_idx
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
char *candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, char *name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
bool has_cycle(int winner, int loser);
void print_winner(void);

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count;
    printf("Number of voters: ");
    scanf("%d", &voter_count);

    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference represented in candidate_idx
        int ranks[candidate_count];

        for (int j = 0; j < candidate_count; j++)
        {
            char name[256];
            printf("Rank %i: ", j + 1);
            scanf("%s", name);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

//A simple variable (Int) has been passed to the function, this is ok as the int will be updated into the array and array will always be passed to functions as memory address
// Update ranks given a new vote
bool vote(int rank, char *name, int ranks[])
{
    for(int i = 0; i < candidate_count; i++)
    {
        if(strcmp(name, candidates[i]) == 0)
        {
            // rank is j in the main - the count the loop is currently at.
            // i is the idx of candidates array.
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for(int i = 0; i < candidate_count; i++)
    {
        for(int j = i + 1; j < candidate_count; j++)
        {
            //starting from the name ranked first, all the following name that comes after is less preferred hence, preferences[candidate_idx ranked first][candidate_idx ranked second..third..] + 1.
            preferences[ranks[i]][ranks[j]]++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for(int i = 0; i < candidate_count; i++)
    {
        for(int j = 0; j < candidate_count; j++)
        {
            if(preferences[i][j] > preferences[j][i])
            {
                pair new_pair = {i, j};
                pairs[pair_count] = new_pair;
                //pair_count initialised to 0 at the beginning.
                pair_count++;
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    int max_idx;
    for(int i = 0; i < pair_count - 1; i++)
    {
        max_idx = i;
        for(int j = i + 1; j < pair_count; j++)
        {
            if(preferences[pairs[j].winner][pairs[j].loser] > preferences[pairs[max_idx].winner][pairs[max_idx].loser])
            {
                max_idx = j;
            }
        }
        pair temp = pairs[i];
        pairs[i] = pairs[max_idx];
        pairs[max_idx] = temp;
    }
    return;
}


// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for(int i = 0; i < pair_count; i++)
    {
        if(!has_cycle(pairs[i].winner, pairs[i].loser))
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }
    return;
}

//A simple variable (Int) has been passed to the function, this is ok as the function checks for lock status and return true/false, it do not update the simple variable in main.
bool has_cycle(int winner, int loser)
{
    //the first loop will never return true, but this serves as termination as loser will be replaced subsequently.
    if(locked[loser][winner] == true)
    {
        return true;
    }
    //checks the rest of candidates if they are locked with loser, if one of them is locked with loser, recursive function replace loser as i and winner unchanged.
    //this will trace the locked pattern till the winner, should there be a cycle.
    for(int i = 0; i < candidate_count; i++)
    {
        if(locked[loser][i] == true && has_cycle(winner, i))
        {
            return true;
        }
    }
    return false;
}

void print_winner(void)
{
    int w = 0;
    for(int i = 0; i < pair_count; i++)
    {
        for(int j = 0; j < pair_count; j++)
        {
            if(locked[j][i] == true)
            {
                break;
            }
            else
            {
                w = i;
            }
        }
    }
    printf("%s\n", candidates[w]);

    return;
}