import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
      </Head>

      <main className={styles.main}>
          <grid className = {styles.grid}>
              <side1 className = {styles.card}>
                    <p1>Hello, I am...</p1>

                    <h1 className={styles.title}>
                        Max Zimmermann
                    </h1>
                  
                    <p className={styles.description}>
                        Student at the <a>University of Ottawa</a>
                    </p>

                    <p1>I'm studying <a>computer science</a> with a minor in <a>physics</a>. Athought that is my main focus right now, I also take on <a>personal projects</a> (such as this website!) to grow my skills in <a>practical applications</a>.
                    <br></br><br></br>I also have a passion for <a>music</a>, including singing and playing the <a>piano and drums</a>. I've made a few original songs, but I prefer to make covers of the songs I'm currently listening to. I hope to <a>grow this passion</a> and become a better and better musician over time.</p1>

              </side1>

              <side2 className = {styles.card}>

                  <h1 className={styles.subtitle}>Socials</h1>

                  <linkgrid className = {styles.smallgrid}>
                    <a className = {styles.YTlinkcard} href='https://www.youtube.com/channel/UCJlbxXNRgRfQhpqk600A9cw'>YouTube</a>
                    <a className = {styles.INlinkcard} href='https://www.instagram.com/max_zimmz/'>Instagram</a>
                    <a className = {styles.SClinkcard} href='https://soundcloud.com/maxx-zimmermann'>Soundcloud</a>
                    <a className = {styles.GHlinkcard} href='https://github.com/Hobomojo38'>GitHub</a>
                  </linkgrid>

              </side2>
          </grid>
      </main>

      <footer className={styles.footer}>
          Made using Next.js
          <br></br>Created by Max Zimmermann, 2022
      </footer>
    </div>
  )
}
