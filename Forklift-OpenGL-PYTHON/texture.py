from __future__ import division
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL import Image

def readImage(path):
    image = Image.open(path)
    (width, height) = image.size
    stringImage = image.tostring("raw", "RGB", 0, -1)
    return (width, height, stringImage)


class Surround(object):
    """
        The courtyard scene for experimenting with texture mapping.
        Adegan halaman untuk bereksperimen dengan pemetaan tekstur.
    """

    
    TEX_FLOOR_REPS = 4
    FLOOR_SIZE = 15
    WALL_HEIGHT = 15

    def glInit(self):
        """
            Set up OpenGL pipeline stuff needed by this particular scene
            Siapkan hal-hal saluran pipa OpenGL yang dibutuhkan oleh adegan khusus ini
        """
        
        # Left Wall Texture
        self.wall_1_id = glGenTextures(1)
        (w,h,pattern) = readImage("assets/left_wall_texture_I.jpg")
        glBindTexture(GL_TEXTURE_2D, self.wall_1_id)
        gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGB, w, h, GL_RGB, GL_UNSIGNED_BYTE, pattern)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glTexEnvi(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE)
        
        # Front Wall Texture
        self.wall_2_id = glGenTextures(1)
        (w,h,pattern) = readImage("assets/front_wall_texture.jpg")
        glBindTexture(GL_TEXTURE_2D, self.wall_2_id)
        gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGB, w, h, GL_RGB, GL_UNSIGNED_BYTE, pattern)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glTexEnvi(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE)
        
        # Right Wall Texture
        self.wall_3_id = glGenTextures(1)
        (w,h,pattern) = readImage("assets/right_wall_texture.jpg")
        glBindTexture(GL_TEXTURE_2D, self.wall_3_id)
        gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGB, w, h, GL_RGB, GL_UNSIGNED_BYTE, pattern)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glTexEnvi(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE)
        
        # Left Wall Texture
        self.wall_4_id = glGenTextures(1)
        (w,h,pattern) = readImage("assets/left_wall_texture_II.jpg")
        glBindTexture(GL_TEXTURE_2D, self.wall_4_id)
        gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGB, w, h, GL_RGB, GL_UNSIGNED_BYTE, pattern)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glTexEnvi(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE)
        
        
        # Floor Texture
        self.floorTextureID = glGenTextures(1)
        (w,h,pattern) = readImage("assets/floor_texture.tga")
        glBindTexture(GL_TEXTURE_2D, self.floorTextureID)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, pattern)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glTexEnvi(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE)
        
        

        
    def walls(self):
        

        # BACK WALL
        glBindTexture(GL_TEXTURE_2D, self.wall_4_id)
        glBegin(GL_QUADS)

        glNormal3f(0, 1, 0)
        
        glTexCoord2f(0, 1)
        glVertex3f(-self.FLOOR_SIZE, self.WALL_HEIGHT, -self.FLOOR_SIZE)
        
        glTexCoord2f(0, 0)
        glVertex3f(-self.FLOOR_SIZE, 0, -self.FLOOR_SIZE)
        
        glTexCoord2f(1, 0)
        glVertex3f(self.FLOOR_SIZE, 0, -self.FLOOR_SIZE)
        
        glTexCoord2f(1, 1)
        glVertex3f(self.FLOOR_SIZE, self.WALL_HEIGHT, -self.FLOOR_SIZE)
        
        glEnd()

        # FRONT WALL
        glBindTexture(GL_TEXTURE_2D, self.wall_2_id)
        glBegin(GL_QUADS)

        glNormal3f(0, 1, 0)
        
        glTexCoord2f(1, 1)
        glVertex3f(-self.FLOOR_SIZE, self.WALL_HEIGHT, self.FLOOR_SIZE)
        
        glTexCoord2f(1, 0)
        glVertex3f(-self.FLOOR_SIZE, 0, self.FLOOR_SIZE)
        
        glTexCoord2f(0, 0)
        glVertex3f(self.FLOOR_SIZE, -0, self.FLOOR_SIZE)
        
        glTexCoord2f(0, 1)
        glVertex3f(self.FLOOR_SIZE, self.WALL_HEIGHT, self.FLOOR_SIZE)
        
        glEnd()

        # LEFT WALL
        glBindTexture(GL_TEXTURE_2D, self.wall_3_id)
        glBegin(GL_QUADS)

        glNormal3f(0, 1, 0)
        
        glTexCoord2f(1, 1)
        glVertex3f(-self.FLOOR_SIZE, self.WALL_HEIGHT, -self.FLOOR_SIZE)
        
        glTexCoord2f(1, 0)
        glVertex3f(-self.FLOOR_SIZE, 0, -self.FLOOR_SIZE)
        
        glTexCoord2f(0, 0)
        glVertex3f(-self.FLOOR_SIZE, 0, self.FLOOR_SIZE)
        
        glTexCoord2f(0, 1)
        glVertex3f(-self.FLOOR_SIZE, self.WALL_HEIGHT, self.FLOOR_SIZE)
        
        glEnd()
        
        # RIGHT WALL

        glNormal3f(0, 1, 0)
        glBindTexture(GL_TEXTURE_2D, self.wall_1_id)
        glBegin(GL_QUADS)
        
        glTexCoord2f(0, 1)
        glVertex3f(self.FLOOR_SIZE, self.WALL_HEIGHT, -self.FLOOR_SIZE)
        
        glTexCoord2f(0, 0)
        glVertex3f(self.FLOOR_SIZE, 0, -self.FLOOR_SIZE)
        
        glTexCoord2f(1, 0)
        glVertex3f(self.FLOOR_SIZE, 0, self.FLOOR_SIZE)
        
        glTexCoord2f(1, 1)
        glVertex3f(self.FLOOR_SIZE, self.WALL_HEIGHT, self.FLOOR_SIZE)

        glEnd()

    

    def floor(self):
        glBindTexture(GL_TEXTURE_2D, self.floorTextureID)
        
        glNormal3f(0, 1, 0)
        glBegin(GL_QUADS);
        
        glTexCoord2f(0, self.TEX_FLOOR_REPS)
        glVertex3f(-self.FLOOR_SIZE, 0, -self.FLOOR_SIZE)
        
        glTexCoord2f(0, 0)
        glVertex3f(-self.FLOOR_SIZE, 0, self.FLOOR_SIZE)
        
        glTexCoord2f(self.TEX_FLOOR_REPS,0)
        glVertex3f(self.FLOOR_SIZE, 0, self.FLOOR_SIZE)
        
        glTexCoord2f(self.TEX_FLOOR_REPS, self.TEX_FLOOR_REPS)
        glVertex3f(self.FLOOR_SIZE, 0, -self.FLOOR_SIZE)
        glEnd()


    def glDisplay(self):
        """
        Output the entire scene to the OpenGL pipeline.
        Mengeluarkan seluruh adegan ke pipa OpenGL
        
        This method is expected to be called by a View object, after the
        model view matrix has been set up for an appropriate view and the
        various buffers cleared.
        Metode ini diharapkan dipanggil oleh objek tampilan, setelah 
        matriks tampilan model telah diatur untuk tampilan yang sesuai 
        dan berbagai buffer dihapus.
        """
        glEnable(GL_TEXTURE_2D)
        glColor3f(1,1,1)
        self.walls()
        self.floor()
        glDisable(GL_TEXTURE_2D)
