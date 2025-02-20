/*
  B-tree sort functions
  Interface package for indexed files
  using the PBL btree library
  The data file is read only
  May 2021. J Garrido
  File:  indxsF2.h
*/  
  
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <errno.h>
#include <stdlib.h>
#include <ctype.h>

#include "pbl.h"

struct idxFile {
    FILE * dataFilep;
    char dataFileName[30];
    char keyFileName[30];
    pblKeyFile_t * keyFile;
    unsigned long total_records; 
    void * datarec;          // pointer to data record 
    unsigned datareclen;
    unsigned int numblk;     // number of blocks
    char * keyf;             // key used 
    unsigned keyflen;
    char * recno;
    unsigned recnolen;
};
typedef struct idxFile indxsT;

/* Create index (key) file  */
int idxsFCreate(indxsT * idxfp, char * dfilepath, char * datafilen, FILE * dataFilep, void * filesettag );
/*
  Open the  key file
  update = 1;     // to write or update. otherwise is 0
*/
int idxsFOpen(indxsT * idxfp, char * openMode, int update );

// Write key record 
int idxsFWrite(indxsT * idxfp);

// Read the next record from data file, by key value
int idxsFReadNext(indxsT * idxfp);

// Read the first record from data file and key file
int idxsFReadFirst(indxsT * idxfp);

// close data file and the corresponding key file 
int idxsFClose (indxsT * idxfp);

