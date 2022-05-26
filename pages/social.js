import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
      <div className={styles.container}> 
        <Head>
            <title>Socials</title>
            <meta name="description" content="Page decicated to me socials"/>
            <link rel="icon" href="/favicon.ico" />
        </Head>

        <main className={styles.main}>

            <h className={styles.titledDivider}>My Socials</h>

            <div className={styles.grid}>

                <div className={styles.thinCard}>
                    <a className = {styles.YTlinkcard} href='https://www.youtube.com/channel/UCJlbxXNRgRfQhpqk600A9cw'>YouTube</a>
                    <a className = {styles.INlinkcard} href='https://www.instagram.com/max_zimmz/'>Instagram</a>
                </div>

                <img src='SnapChat Code.jpg' width='300'></img>

                <div className={styles.thinCard}>
                    <a className = {styles.SClinkcard} href='https://soundcloud.com/maxx-zimmermann'>Soundcloud</a>
                    <a className = {styles.GHlinkcard} href='https://github.com/Hobomojo38'>GitHub</a>
                </div>

            </div>
        </main>
      
      </div>
  )
}