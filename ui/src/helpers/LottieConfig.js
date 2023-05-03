const defaultOptionsLottie = (animationData) => {
  return {
    loop: true,
    autoplay: true,
    animationData,
    rendererSettings:
      {
        preserveAspectRatio: 'xMidYMid slice'
      }
  }
}

export default defaultOptionsLottie
