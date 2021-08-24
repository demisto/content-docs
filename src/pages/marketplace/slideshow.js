import React from 'react';
import { Slide } from 'react-slideshow-image';
import 'react-slideshow-image/dist/styles.css'
import Link from "@docusaurus/Link";
import image1 from './new_images/Marketplace_Vertical_1.png';
import image2 from './new_images/Marketplace_Vertical_2.png';
import image3 from './new_images/Marketplace_Vertical_3.png';


const slideImages = [
  {
    url: image1, //'https://raw.githubusercontent.com/demisto/content-docs/148c5a9e7153b1688acb2f331b414e30a3f75f8c/src/pages/marketplace/images/Marketplace_Vertical_1.png',
    caption: 'Slide 1',
    link: 'https://start.paloaltonetworks.com/join-our-slack-community'
  },
  {
    url: image2, //'https://raw.githubusercontent.com/demisto/content-docs/148c5a9e7153b1688acb2f331b414e30a3f75f8c/src/pages/marketplace/images/Marketplace_Vertical_2.png',
    caption: 'Slide 2',
    link: 'https://start.paloaltonetworks.com/cortex-xsoar-whats-soaring-newsletter.html'
  },
  {
    url: image3, //'https://raw.githubusercontent.com/demisto/content-docs/148c5a9e7153b1688acb2f331b414e30a3f75f8c/src/pages/marketplace/images/Marketplace_Vertical_3.png',
    caption: 'Slide 3',
    link: 'https://www.paloaltonetworks.com/cortex/xsoar'
  }
];

const Slideshow = () => {
  return (
    <div className="slide-container">
      <Slide>
       {slideImages.map((slideImage, index)=> (
          <div className="each-slide" key={index}>
            <Link to={slideImage.link}>
            <img className="slideimg" src={slideImage.url} alt="sample"/>
            </Link>
          </div>
        ))} 
      </Slide>
    </div>
  )
}

export default Slideshow;