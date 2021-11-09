# Flickr parser
> Can intelligently download images using freely specified tags.<br>
> Also it has a tensorflow add-on for filtering photos by the parameters of people's faces.

![](img/header.jpg)

## Usage
1. Create Flickr API key and secret [here](https://www.flickr.com/services/apps/create/apply/)
2. Pass it to ```.env``` file
3. Install project requirements
4. Change variables in ```main.py``` depending on your task
5. Run ```main.py```

## Installing of requirements
```sh
pip install -r requirements.txt
```

## Default task
* Download 1000 photos
* Each image contains exactly one human face
* The size of the face is at least 256x256 pixels
* The person in the photo is wearing glasses

## Examples of parsed items
![](img/29110461261_0fd9933b0d_o.jpg)
![](img/2707013695_48b94e9220_o.jpg)
![](img/49416467796_fbd3b980cf_k.jpg)

## Description of pipeline
Data collects via official Flickr API.
At the same time, images passes through filter that uses a [mtcnn](https://github.com/ipazc/mtcnn) library (works with TensorFlow).<br>
In the default task, I control the number of faces and size of the box framing the person's face in the picture.

## Authors
* [Gleb Savelev](https://github.com/nardo-leo)

## Contributing
1. Fork it
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
