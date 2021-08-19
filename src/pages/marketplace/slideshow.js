import React from 'react';
import { Slide } from 'react-slideshow-image';
import 'react-slideshow-image/dist/styles.css'
import Link from "@docusaurus/Link";
import image1 from "./images/Marketplace_Vertical_1.png";
import image2 from "./images/Marketplace_Vertical_2.png";
import image3 from "./images/Marketplace_Vertical_3.png";


const slideImages = [
  {
    url: image1,
    caption: 'Slide 1',
    link: 'https://start.paloaltonetworks.com/join-our-slack-community'
  },
  {
    url: image2,
    caption: 'Slide 2',
    link: 'https://start.paloaltonetworks.com/cortex-xsoar-whats-soaring-newsletter.html'
  },
  {
    url: image3,
    caption: 'Slide 3',
    link: 'https://www.paloaltonetworks.com/cortex/xsoar'
  }
];

const properties = {
  duration: 5000,
  transitionDuration: 500,
  infinite: true,
  indicators: true,
  scale: 0.4,
  arrows: true
}

const Slideshow = () => {
  return (
    <div className="slide-container">
      <Slide>
       {slideImages.map((slideImage, index)=> (
          <div className="each-slide" key={index}>
            <Link to={slideImage.link}>
            <img className="lazy" src={slideImage.url} alt="sample" />
            </Link>
          </div>
        ))} 
      </Slide>
    </div>
  )
}

export default Slideshow;