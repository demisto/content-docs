import { useLocation } from "@docusaurus/router";
import React, { useEffect } from "react";


function Marketplace() {
  const location = useLocation();
  const newLocation = location.search
    ? `https://cortex.marketplace.pan.dev/marketplace/${location.search}`
    : "https://cortex.marketplace.pan.dev/marketplace";

  useEffect(() => {
    if (! (location.search.endsWith('contributors'))) {
        window.location.href = newLocation;
    }
  }, []);

  return (
    <span>
      Redirecting to Cortex XSOAR Marketplace... click{" "}
      <a target="_self" href={newLocation}>
        here
      </a>{" "}
      if the redirect fails or is taking too long.
    </span>
  );
}

export default Marketplace;