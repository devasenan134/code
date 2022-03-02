
from IPython.display import HTML
from demo import load_checkpoints
generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml', 
                            checkpoint_path='/content/gdrive/MyDrive/Colab Notebooks/vox-adv-cpk.pth.tar')

import imageio
from demo import make_animation
from demo import display
from skimage import img_as_ubyte
from IPython.display import HTML

source_image = imageio.imread(
    'deep_fake/Trump.jpg')
driving_video = imageio.mimread('deep_fake/obama_speech.mp4', memtest=False)

predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True)

# save resulting video
## imageio.mimsave('../generated.mp4', [img_as_ubyte(frame) for frame in predictions], fps=fps)
#video can be downloaded from /content folder

HTML(display(source_image, driving_video, predictions).to_html5_video())
