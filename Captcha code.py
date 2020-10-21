#!/usr/bin/env python
# coding: utf-8

# # 1. Image Captcha

# In[ ]:


#Import necessary module


# In[13]:


from captcha.image import ImageCaptcha

image = ImageCaptcha(width = 270, height = 90)
data = image.generate("CCCCVGFD")
image.write('CCCCVGFD','demo2.png')


# In[10]:


from captcha.image import ImageCaptcha

image = ImageCaptcha(width = 280, height = 90)
data = image.generate("BHBHGFFDD")
image.write('BHBHGFFDD','demo3.png')


# In[16]:


from captcha.image import ImageCaptcha

image = ImageCaptcha(width = 270, height = 80)
data = image.generate("12CCP890")
image.write('12CCP890','demo4.png')


# # Audio Captcha

# In[27]:


from captcha.audio import AudioCaptcha

audio = AudioCaptcha()
data = audio.generate("99898")
audio.write('99898','demo6.wmv')


# In[ ]:




