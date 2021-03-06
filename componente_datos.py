#!/usr/bin/python
# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import sys, pygame
from os import system

class comp_dat_arg(pygame.sprite.Sprite):
    posic_rel_x=0
    posic_rel_y=0
    pulsado=0
    posicion=(0,0)
    cadena_final=""
    cadena_intermedia=""
    #rectangulo que representa toda el area del componente
    rectan=pygame.Rect(0,0,80,40)
    ide=0
    color=(125,100,83)
    modificable=0
    valor_cadena_no_mod="0"

    def __init__(
                    self,
                    x,y,
                    identidad,
                    mod,
                    texto,
                    color,
                    val_no_mod,
                    img,
                    tipo,
                    fondo,
                    ventana,
                    textorender
                ):
        pygame.sprite.Sprite.__init__(self)
        self.ide=identidad
        self.posicion=(x,y)
        self.texto=texto
        self.color=color
        self.fondo=fondo
        self.ventana=ventana
        self.textorender=textorender
        self.color_texto=self.fondo.color_texto
        self.conector_m=pygame.Rect(0,0,10,20)#conector macho
        self.conector_h=pygame.Rect(0,0,10,20)#conector hembra
        self.pegado2=0
        self.pegado_a2=0
        self.pegado=0
        self.pegado_a=0
        self.pegado_b=0
        self.conectado=0
        self.tecla=0
        self.tecla_presionada=0
        self.modificable=mod
        self.valor_cadena_no_mod=val_no_mod
        self.tipo=tipo
        if self.tipo==6:
            self.imagenintermedia=img
            self.img=sys.path[0] +"/imagenes/componentes/"+ img
            self.imagen=pygame.image.load(self.img)
            self.img_rect=self.imagen.get_rect()
    def dibujar(self):
        #tomo el valor del texto para agrandar el tamaño del
        # cuerpo del componente.
        # si es una imagen le pongo un valor fijo
        TamaComp=0
        if self.tipo==7:
            TamaComp=len(self.texto)
        else:
            TamaComp=3
        #cubos que representan el conector hembra
        pygame.draw.rect(
                        self.fondo.screen,
                        self.color,
                        (
                        self.posicion[0]+30+(7*TamaComp),
                        self.posicion[1]-10,
                         10,
                         10
                         ),
                        0
                        )
        pygame.draw.rect(
                        self.fondo.screen,
                        self.color,
                        (
                        self.posicion[0]+30+(7*TamaComp)+3,
                        self.posicion[1],
                         4,
                         4
                         ),
                        0
                        )
        pygame.draw.rect(
                        self.fondo.screen,
                        self.color,
                        (
                        self.posicion[0]+30+(7*TamaComp),
                        self.posicion[1]+20,
                        10,
                        10
                        ),
                        0
                        )
        pygame.draw.rect(
                        self.fondo.screen,
                        self.color,
                        (
                        self.posicion[0]+30+(7*TamaComp)+3,
                        self.posicion[1]+20-4,
                         4,
                         4
                         ),
                        0
                        )
        self.conector_h[0]=self.rectan[0]+30+(7*TamaComp)
        self.conector_h[1]=self.rectan[1]
        # conector macho
        pygame.draw.rect(
                        self.fondo.screen,
                        self.color,
                        (
                        self.posicion[0],
                        self.posicion[1]+4,
                        10,
                        20-8
                        ),
                        0
                        )
        pygame.draw.rect(
                        self.fondo.screen,
                        self.color,
                        (
                        self.posicion[0],
                        self.posicion[1],
                        3,
                        20
                        ),
                        0
                        )
        pygame.draw.rect(
                        self.fondo.screen,
                        self.color,
                        (
                        self.posicion[0]+7,
                        self.posicion[1],
                        3,
                        20
                        ),
                        0
                        )
        # cuerpo del componente
        pygame.draw.rect(
                        self.fondo.screen,
                        self.color,
                        (
                        self.posicion[0]+10,
                        self.posicion[1]-10,
                        7*TamaComp+20,
                        40
                        ),
                        0
                        )
        self.rectan[2]=7*TamaComp+20
        if self.tipo==7:
            self.textorender.render(
                                    str(self.texto),
                                    self.color_texto,
                                    (
                                    (self.posicion[0]+20),
                                    (self.posicion[1]+5)
                                    )
                                    )
        if self.tipo==6:
            self.modificable=0
            self.fondo.screen.blit(
                                self.imagen,
                                (
                                self.posicion[0]+30-(
                                                    self.img_rect[2]/2
                                                    ),
                                self.posicion[1]-5
                                )
                                )

    def update(self):
        ban_a=0
        cadena_auxiliar=""
        posic_mouse= self.ventana.mousexy
        botones_mouse = self.ventana.boton_mouse
        # self.rectan es el rect
        # que representa la totalidad de la figura
        self.rectan[0]=self.posicion[0]
        self.rectan[1]=self.posicion[1]
        # self.conector_m es la ficha "macho"
        self.conector_m[0]=self.rectan[0]
        self.conector_m[1]=self.rectan[1]
        if (
            botones_mouse[1] and
            self.rectan.collidepoint(posic_mouse[0],posic_mouse[1]) and
            self.modificable==1 and
            self.ventana.seleccion_menu==4
            ):
            print "habilito la edicion del boton"
            self.tecla=1
            self.ventana.seleccionado_datos_ed=self.ide
            self.texto=""
        if self.tecla==1 and self.ventana.seleccionado_datos_ed==self.ide:
            if self.valor_cadena_no_mod=="a":
                if (self.tecla_presionada==1 and self.ventana.tecla==1):
                    cadena_auxiliar= self.ventana.valor_tecla
                    self.tecla_presionada=0
                    if cadena_auxiliar!="":
                        self.texto = self.texto + cadena_auxiliar
            if self.valor_cadena_no_mod=="0":
                if (self.tecla_presionada==1 and 
                    self.ventana.tecla==1 and
                    self.ventana.valor_tecla.isdigit()):
                    cadena_auxiliar= self.ventana.valor_tecla
                    self.tecla_presionada=0
                    if cadena_auxiliar!="":
                        self.texto = self.texto + cadena_auxiliar
            if self.ventana.tecla==0:
                self.tecla_presionada=1
            if self.ventana.tecla_enter==1:
                self.tecla=0
                self.ventana.seleccionado_datos_ed=0
        if self.modificable==1:
            self.cadena_final=self.texto+self.cadena_intermedia
        else:
            self.cadena_final=  (
                                self.valor_cadena_no_mod
                                +
                                self.cadena_intermedia
                                )
        self.cadena_final=self.cadena_final.replace("\r", '')

        if self.conectado==0:
            if self.pegado==0:
                for a in range(1,len(self.fondo.objetos)):
                    valor1=self.fondo.objetos[a].lista_conector_h_datos
                    for b in range(len(valor1)):
                        valor2=self.fondo.objetos[a]
                        valor3=valor2.lista_conector_h_datos[b]
                        if (self.conector_m.colliderect(valor3)):
                            self.pegado=1
                            self.conectado=1
                            self.pegado_a=a
                            self.pegado_b=b
        if self.pegado==1:
            valor1=self.fondo.objetos[self.pegado_a]
            valor2=valor1.lista_conector_h_datos[self.pegado_b]
            x,y,aa,bb=valor2
            xx=x
            yy=y
            self.posicion=(xx,yy)
            valor1.lista_valores[self.pegado_b]=self.cadena_final
        if self.conectado==0:
            if self.pegado2==0:
                for z in range(1,len(self.fondo.objetos_datos)):
                    val=self.fondo.objetos_datos[z].conector_h
                    if self.conector_m.colliderect(val):
                        self.pegado_a2=z
                        self.pegado2=1
                        self.conectado=1
        if self.pegado2==1:
            val1=self.fondo.objetos_datos[self.pegado_a2].conector_h
            x,y,aa,bb=val1
            xx=x
            yy=y
            self.posicion=(xx,yy)
            val2=self.fondo.objetos_datos[self.pegado_a2]
            val2.cadena_intermedia=self.cadena_final
        else:
            self.cadena_intermedia=""
        if (
            botones_mouse[1]==1 and
            self.rectan.collidepoint(self.ventana.mousexy) and
            self.pulsado==0 and
            self.ventana.seleccionado_datos==0
            ):
            posic_mouse= self.ventana.mousexy
            self.ventana.seleccionado_datos=self.ide
            self.posic_rel_x=abs(self.posicion[0]-posic_mouse[0])
            self.posic_rel_y=abs(self.posicion[1]-posic_mouse[1])
            self.pulsado=1
        if self.ventana.seleccionado_datos== self.ide:
            self.posicion=(
                            posic_mouse[0]-self.posic_rel_x,
                            posic_mouse[1]-self.posic_rel_y
                            )
            self.conectado=0
            self.pegado=0
            self.pegado_a=0
            self.pegado_b=0
            self.pegado2=0
            self.pegado_a2=0
        if botones_mouse[1]==0:
            self.pulsado=0
            self.ventana.seleccionado_datos=0
        if (botones_mouse[1]==1
                and self.rectan.collidepoint(self.ventana.mousexy)
                and self.ventana.seleccion_menu==3):
            for i in range(1,len(self.fondo.objetos_datos)):
                self.fondo.objetos_datos[i].conectado=0
                self.fondo.objetos_datos[i].pegado=0
                self.fondo.objetos_datos[i].pegado_a=0
                self.fondo.objetos_datos[i].pegado_b=0
                self.fondo.objetos_datos[i].pegado2=0
                self.fondo.objetos_datos[i].pegado_a2=0
            a=self.fondo.objetos_datos.index(self)
            ident=self.fondo.objetos_datos[a].ide

            del self.fondo.tipo_obj_datos[a]
            self.kill()
            self.fondo.objetos_datos.remove(self)
        self.dibujar()
        self.cadena_intermedia=""
        if self.pegado==1:
            ob=self.fondo.objetos
            x,y,aa,bb=ob[self.pegado_a].lista_conector_h_datos[self.pegado_b]
            xx=x
            yy=y
            self.posicion=(xx,yy)
            self.fondo.objetos[self.pegado_a].lista_valores[self.pegado_b]=self.cadena_final
        if self.conectado==0:
            if self.pegado2==0:
                for z in range(1,len(self.fondo.objetos_datos)):
                    if self.conector_m.colliderect(self.fondo.objetos_datos[z].conector_h):
                        self.pegado_a2=z
                        self.pegado2=1
                        self.conectado=1
        if self.pegado2==1:

            x,y,aa,bb=self.fondo.objetos_datos[self.pegado_a2].conector_h
            xx=x
            yy=y
            self.posicion=(xx,yy)
            self.fondo.objetos_datos[self.pegado_a2].cadena_intermedia=self.cadena_final

        if botones_mouse[1]==1 and self.rectan.collidepoint(self.ventana.mousexy) and self.pulsado==0 and self.ventana.seleccionado_datos==0:
            posic_mouse= self.ventana.mousexy
            self.ventana.seleccionado_datos=self.ide
            self.posic_rel_x=abs(self.posicion[0]-posic_mouse[0])
            self.posic_rel_y=abs(self.posicion[1]-posic_mouse[1])
            self.pulsado=1
        if self.ventana.seleccionado_datos== self.ide:
            self.posicion=(posic_mouse[0]-self.posic_rel_x,posic_mouse[1]-self.posic_rel_y)
            self.conectado=0
            self.pegado=0
            self.pegado_a=0
            self.pegado_b=0
            self.pegado2=0
            self.pegado_a2=0
            #self.pulsado==1
        if botones_mouse[1]==0:
            self.pulsado=0
            self.ventana.seleccionado_datos=0

        if (botones_mouse[1]==1
                and self.rectan.collidepoint(self.ventana.mousexy)
                and self.ventana.seleccion_menu==3):
            for i in range(1,len(self.fondo.objetos_datos)):
                self.fondo.objetos_datos[i].conectado=0
                self.fondo.objetos_datos[i].pegado=0
                self.fondo.objetos_datos[i].pegado_a=0
                self.fondo.objetos_datos[i].pegado_b=0
                self.fondo.objetos_datos[i].pegado2=0
                self.fondo.objetos_datos[i].pegado_a2=0
            #~ a=self.fondo.objetos_datos.index(self)
            #~ ident=self.fondo.objetos_datos[a].ide
                #~ for i in range(len(self.fondo.objetos)):
                    #~ self.fondo.objetos[i].pegado_a=0
                    #~ self.fondo.objetos[i].pegado=0
                #~ self.fondo.objetos_datos[a].vivo=False
            #~ del self.fondo.tipo_obj_datos[a]
            self.kill()
            #~ self.fondo.objetos_datos.remove(self)
                #~ self.fondo.lista_ordenada[self.ide]=0
        self.dibujar()
        self.cadena_intermedia=""
        #pygame.display.update
