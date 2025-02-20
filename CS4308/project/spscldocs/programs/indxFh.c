//SPSCL v1.0 File: indxFh.c, Sun Aug 07 21:38:07 2022
 
/*
  Interface package for indexed files
  using the PBL btree library
  May 2021. J Garrido
  File:  indxFh.scl */  
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <errno.h> 
#include <stdlib.h> 
#include <ctype.h> 
#include "pbl.h" 
// specifications 
struct idxFile 
{
char  dataFileName[30]; 
 char  keyFileName[30]; 
 FILE *  dataFilep; 
 pblKeyFile_t *  keyFile; 
 
}; // end struct idxFile 
 typedef struct idxFile idxFileT;
struct param_record 
{
void  *  datarec; 
 unsigned int  datareclen; 
 unsigned int  numblk; 
 char  *  keyf; 
 unsigned int  keyflen; 
 char  *  recno; 
 unsigned int  recnolen; 
 int  ival; 
 
}; // end struct param_record 
 typedef struct param_record precT;
// forward declarations 
 // Create a data file and its corresponding index (key) file   
 // Open the data file and corresponding key file 
 int  idxFCreate( idxFileT *  idxfp, char  *  dfilepath, void  *  filesettag ); 
 //  update = 1;     // to write or update. otherwise is 0 
 int  idxFOpen( idxFileT *  idxfp, char  *  openMode, int  update ); 
 // Write data record and corresponding key record 
 int  idxFWrite( idxFileT *  idxfp, precT *  precPtr ); 
 // Given a key value, find and read the record from data file 
 int  idxFReadRec( idxFileT *  idxfp, precT *  precPtr ); 
 // Read the next record from data file, by key value 
 int  idxFReadNext( idxFileT *  idxfp, precT *  precPtr ); 
 // Read the first record from data file and key file 
 int  idxFReadFirst( idxFileT *  idxfp, precT *  precPtr ); 
 // Delete a record given its key, from the data file and from the key file 
 int  idxFDeleteRec( idxFileT *  idxfp, precT *  precPtr ); 
 // close data file and thye corresponding key file  
 int  idxFClose( idxFileT *  idxfp ); 
