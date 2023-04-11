// Declares a dictionary's functionality

//ensures that even though dictionary.c and speller.c #include this file, clang will only compile it once.
#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>

// Maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45

// Prototypes
bool check(const char *word);
unsigned int hash(const char *word);
bool load(const char *dictionary, unsigned int *numberofwords);
unsigned int size(unsigned int numberofwords);
bool unload(void);

#endif // DICTIONARY_H
