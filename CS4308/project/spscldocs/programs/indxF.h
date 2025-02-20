/*
  Interface package for indexed files
  using the PBL btree library
  May 2021. J Garrido
  File:  indxF.h
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
	void * datarec;
	unsigned datareclen;
	unsigned int numblk;
	char * keyf;
	unsigned keyflen;
	char * recno;
	unsigned recnolen;
	int ival;
};

typedef struct idxFile idxFileT;


/* Create a data file and its corresponding index (key) file  */
int idxFCreate(idxFileT * idxfp, char * dfilepath, void * filesettag );
/*
  Open the data file and corresponding key file
  update = 1;     // to write or update. otherwise is 0
*/
int idxFOpen(idxFileT * idxfp, char * openMode, int update );
// Write data record and corresponding key record
int idxFWrite(idxFileT * idxfp);
// Given a key value, find and read the record from data file
int idxFReadRec(idxFileT * idxfp);
// Read the next record from data file, by key value
int idxFReadNext(idxFileT * idxfp);
// Read the first record from data file and key file
int idxFReadFirst(idxFileT * idxfp);
// Delete a record given its key, from the data file and from the key file
int idxFDeleteRec(idxFileT * idxfp);

// close data file and thye corresponding key file 
int idxFClose (idxFileT * idxfp);

