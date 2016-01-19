/*********************************************************************************
* Copyright (C) 2015 Alexey V. Akimov
*
* This file is distributed under the terms of the GNU General Public License
* as published by the Free Software Foundation, either version 2 of
* the License, or (at your option) any later version.
* See the file LICENSE in the root directory of this distribution
* or <http://www.gnu.org/licenses/>.
*
*********************************************************************************/
/**
  \file NList.h
  \brief The file describes auxiliary and main functions for the neighbor list construction
    
*/

#ifndef NList_H
#define NList_H

#include "Cell.h"

/// libcell namespace
namespace libcell{

// Auxiliary functions
void max_vector(VECTOR& t1,VECTOR& t2,VECTOR& t3,VECTOR& T);
void apply_pbc(MATRIX3x3& H,int sz, VECTOR* in, VECTOR* out,vector<quartet>& T);
void serial_to_vector(int c,int Nx,int Ny,int Nz,int& nx,int& ny,int& nz);
void serial_to_vector_symm(int c,int Nx,int Ny,int Nz,int& nx,int& ny,int& nz);
void form_neibc(int c,vector<int>& neibc,int Nx,int Ny,int Nz,double cellx,double celly,double cellz,double Roff);
void find_min_shell(VECTOR& t1,VECTOR& t2,VECTOR& t3,VECTOR& g1,VECTOR& g2,VECTOR& g3,double Roff, triple& minb,triple& maxb);

// Main function
void make_nlist(int Nat,VECTOR* r,MATRIX3x3& H,
                    int maxa,int maxb,int maxc,double cellx,double celly,double cellz,
                    double Roff,vector< vector<quartet> >& nlist_final);
void make_nlist_auto(int Nat,VECTOR* r,MATRIX3x3& H,
                     double cellx,double celly,double cellz,
                     double Roff,vector< vector<quartet> >& nlist);

// For verification purposes
void bruteforce(int Nat,VECTOR* r,MATRIX3x3& H,int maxa,int maxb,int maxc,double Roff,vector< vector<quartet> >& nlist);
double energy(int Nat,VECTOR* r,MATRIX3x3& H,vector< vector<quartet> >& nlist);


}//namespace libcell

#endif // NList_H
