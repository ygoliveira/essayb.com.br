import './Footer.css'

export default function Footer() {

  // functions
  const toTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  // render
  return (
    <div className="footer py-5 text-center border-top text-secondary">
      <div>
        <span>Essay Blog develop by </span>
        <a href="https://github.com/Jmarcelo98">Jmarcelo98</a><span>/</span>
        <a href="https://github.com/Mat123Reis">Mat123Reis</a><span>/</span>
        <a href="https://github.com/senavs">senavs</a><span>/</span>
        <a href="https://github.com/ygoliveira">ygoliveira</a><span>.</span>
      </div>
      <div>
        <span className="to-top text-primary" onClick={toTop}>Back to top</span>
      </div>
    </div>
  )
}