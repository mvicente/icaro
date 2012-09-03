/*-------------------------------------------------------------------------
  stdbool.h - ANSI functions forward declarations

   Ported to PIC16 port by Raphael Neider <rneider AT web.de> (2005)
   
             Written By -  Maarten Brock, sourceforge.brock@dse.nl (2004)

   This library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License, or (at your option) any later version.

   This library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with this library; if not, write to the Free Software
   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
-------------------------------------------------------------------------*/

/*
** $Id: stdbool.h 4148 2006-05-01 20:47:12Z tecodev $
*/

#ifndef __PIC16_STDBOOL_H
#define __PIC16_STDBOOL_H 1

#define _Bool unsigned char

#define bool _Bool
#define true 1
#define false 0
#define __bool_true_false_are_defined 1

#define BOOL unsigned char

#endif  /* __PIC16_STDBOOL_H */