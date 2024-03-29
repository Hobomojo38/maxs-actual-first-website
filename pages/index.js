import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
      <title>Max Zimmermann</title>
        <meta name="description" content="Max Zimmermanns website"/>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      {/* <div className={styles.parallax}>
        <div className={styles.parallax__layer} data-depth="0.6">
          <img src="Centenial Flame Photo.jpg" alt="Layer 1" />
        </div>
        <div className={styles.parallax__layer} data-depth="0.4">
          <img src="Polygonal_Fish.jpg" alt="Layer 2" />
        </div>
      </div> */}


      <main className={styles.main} >
        <div className = {styles.grid}>
          <div className = {styles.titleCard}>
            <p1>Hello, my name is...</p1>

            <h1 className={styles.title}>Max Zimmermann</h1>

            <p className={styles.subtitle}>Programmer, Musician, and University Student</p>

            <p1>
            I am currently studying <r>computer science</r> and <r>physics</r> at the <r>University of Ottawa</r>.
            On top of my studies, I also take on <a>personal projects</a> (such as this website!) to grow my skills in <a>practical applications</a>, many of which are centered around <r>app development</r> as well as <r>music</r>.
            I'm always looking for new projects to undertake and welcome the challenge of <r>pushing my comfort zone</r>.

            <br></br><br></br>


            </p1>

          </div>

          <div className = {styles.card}>
            <h1 className={styles.altTitle}>My Social Media</h1>

            <linkgrid className = {styles.smallgrid}>
              <a className = {styles.YTlinkcard} href='https://www.youtube.com/channel/UCJlbxXNRgRfQhpqk600A9cw'>YouTube</a>
              <a className = {styles.INlinkcard} href='https://www.instagram.com/max_zimmz/'>Instagram</a>
              <a className = {styles.SClinkcard} href='https://soundcloud.com/maxx-zimmermann'>Soundcloud</a>
              <a className = {styles.GHlinkcard} href='https://github.com/Hobomojo38'>GitHub</a>
            </linkgrid>

          </div>
        </div>

        <div className = {styles.titledDivider}>Projects</div>

        <div className={styles.card}>
          <p>Here I have written about some of my past projects. Each post is half-explaination and half-blogpost. Enjoy!</p>
        </div>

        <div className={styles.grid}>

          <div className={styles.card}>
            <r>May 25, 2022</r>
            <div className={styles.subtitle}>Perlin Noise Maze Solver</div>
            <p> I took a trip to Vancouver this week for my brother's bachelor party (Congrats, Karl!). This meant I had two 5-hour flights and two
              12-hour bus rides, and therefore, I wanted to take up a project. I'd watched a video about perlin noise and in my usual hubris, I 
              thought it wouldn't be that hard to set up. I was wrong. <br></br><br></br>

              Step 1: Learn how to make perlin noise. A quick readthrough of the <a href='https://en.wikipedia.org/wiki/Perlin_noise'>Wikipedia Page</a> and 
              a few YouTube walkthoughts gave me a pretty good idea of how the algorithm works. After a couple attempts and a few 
              facepalms, I got the algorithm working and even implimented a GUI to show perlin like it usually it is, a map. <br></br><br></br>

              Step 2: Impliment A* algorithm. As I've learned is common with java, the hard part of this was the setup more than the actual 
              implimentation. Getting the Queue and Node classes to work took a while, but once that was done, I basicaly coded the rest on 
              my first try. <br></br><br></br>

              Althought I technically finished the project, I'm not sure if it came out how I wanted it to. I don't know if I could have 
              done more than I did or if I was just distracted with this being done inbetween events on one of the best weekends I've ever 
              had. Either way, I just don't think my heart was into it by the end and I more so wanted to get it done than do it well. <br></br><br></br>

              Regardless, I'm still proud of what I made. You can download the code <a href='Maxs_Perlin_Pathfinding.zip'>here</a>.

            </p>
          </div>

          <div className={styles.card}>
            <r>May 14th, 2022</r>
            <div className={styles.subtitle}>Personal/Professional Website</div>
            <p> In an effort to try and expand my web development skills, I made this website. I guess that's kind of like learning to swim by jumping into the deep end,
              but I've already had a bit of experience with HTML, so it was just CSS, Next.js, and the various domains needed to run it. I'm pretty proud with how it turned out,
              and hopefully I can maintain it throughout the years as my skills continue to grow (alongside my list of projects...) <br></br><br></br> 
              
              Also, credit where credit is due, this site was in no small way inspired by my friends Emilien and Reid's websites. I've borrowed some elements from both, 
              so thank you guys for doing all the hard work that I can now take credit for!
            </p>
          </div>

          <div className={styles.card}>
            <r>December 6th, 2021</r>
            <div className={styles.subtitle}>AWS Minecraft Server</div>
            <p> I've played minecraft since I was 10 or 11 years old, and while I'm not as enraptured by the game now as I was then, I still enjoy the social aspect of playing alongside my friends.
              However, this requires a external, 3rd-party server everyone can join that usually requires a monthly fee to keep up. I'd heard about AWS before, so I figured I
              would get familiar with it by building a private minecraft server using their Instances.<br></br><br></br>

              It took a few days, but eventually I got it up and operational. You could activate the server by visiting a webpage, at which point a 5 hour 
              countdown would start to eventually shut the server back down. Althought I wish I had more control options for users such as instant shut-down, I'm happy with how it turned out and I actually used it 
              for the duration of that December. Unfortunately, it ended the same way all private minecraft servers do: a surge of excitement at the beginning only to fizzle out to nothing within
              3 weeks. Tis the life of a server, oh well... <br></br><br></br>

              Even so, I learned so much from this project. Not just how to use AWS, but how to work with Bash prompts and text-only interfaces. I had to develop .service files 
              and learn about (some...) automatic server processes. This was my first taste into servers and web applications, and overall, I'm pretty happy with how it turned out.
            </p>
          </div>

          <div className={styles.card}>
            <r>Nov 13th, 2021</r>
            <div className={styles.subtitle}>Conway's Game of Life</div>
            <p> Conway's Game of Life: an interesting mathematical idea turned into fringe computer science-geek knowledge. It's only a matter of time before any programmer takes a crack at 
              it themselves. I coded my version in Python for the explicit reason I could use Pygame, a Python package, to display the cells. I'll be damned if I have to learn how to create 
              a display screen, so Pygame take the reigns, and leave the math to me. <br></br><br></br>

              Although it was not a terribly hard project, it was quite satifsying to watch the end result once I was finished. Having gained a lot of insperation for coding from watching 
              code people on YouTube, it's fun to compare myself to those people and see where I land. This project was one such case, and I'm happy with how it turned out. I even added the 
              ability to activate cells by clicking on them (The generations occur too fast to really see the affect, but if you click beside already active cells, you can see the affect) and 
              a secret "chaos mode" you can activate in the code. It gives you a live count of the time it takes to calculate each generation and render it.<br></br><br></br>

              All in all, a super fun project I really enjoyed doing and would love to incorperate wherever I can. It's kind of an easter egg in computer culture, and a fun in-joke to have 
              taken part in. <br></br><br></br>
              
              You can download the .py file <a href="Conways Game of Life.py" download="Max's Game of Life.py">here</a>. You will need to have both Python and Pygame installed to run it.
            </p>
          </div>

          <div className={styles.card}>
            <r>October 18th, 2021</r>
            <div className={styles.subtitle}>Twitch Datamine Payout Decoder</div>
            <p> Around this time, Twitch, one of the largest live-streaming platforms at the time, was the subject of a massive datamine which leaked the payout amounts to the largest 
              creators on the platform from the past 3 years. I managed to find the original datamine and decided to try and see if I could get those payout numbers for myself (Spolier alert:
              I did... kinda....) <br></br><br></br>

              All the data was contained within compressed .csv files, each entry having just 2 numbers: the amount paid, and the ID of the user it was paid to. Small issue: that ID is
              not their username, it's a random string associated with the users account. Not good. This meant I would have to send each individual name to Twitch's API to get the
              account's username. As well, there was about 30 total .csv files (one for every month of the past 3 years), each containing hundreds of thousands of entrys. In the end, 
              it took me a couple hours to write the code and 48+ hours for it to finish running. And what did I get?<br></br><br></br>

              Basicaly nothing. I found the payouts of the biggest streamers, but they were off from what the general concensus was. I was close, but I had messed up somewhere and I couldn't 
              care enough to try and fix the problem just to have to wait another 2 days to let it run. Although I wouldn't call the project a failure, I'd say it was something worse: pointless. 
              I didn't get anything cool out of it, I didn't get the satifaction of a completed project, and at it's core, the project was just boring. So what if I got the payouts? I could 
              already find them. It wasn't hard to code, and I wouldn't say I learned anything new (maybe .csv file formats, but they aren't that hard to begin with...). I didn't get a 
              satifying end to this project, but at the very least, I had fun. This was a junk-food project. And for was it was, I enjoyed it. That's it, that's all.
            </p>
          </div>

          <div className={styles.card}>
            <r>Augest 24th, 2020</r>
            <div className={styles.subtitle}>Raycasting Graphics Engine</div>
            <p> This was the first major project I ever took one, and the one that got me hooked on programming. The project involved creating a raycasting graphics engine, and type of 
              graphics engine used in games such as Wolfenstien 3D and Doom. One of the first methods to create 3D graphics, it functions as follows: For each line of pixel on the user's 
              screen, it measures the distance between the player and the nearest wall. The farther away the wall, the shorter the line of that columns will be. Fill every pixel above the 
              horizon (The center horizontal line of the screen) with a light colour and every pixel below with a dark colour, and you've now got a basic graphics engine.<br></br><br></br>

              Coding this envolved a lot of math, and while not necessarily complicated math, it was my first time applying math outside of the classroom. Intersecting lines, inverse functions, 
              triginomic functions all optimized to run hundreds of times every second. Dispite this, I still found it immensely satisfying to work through all the problems and turn my 
              personal math algorithms into computable problems with computable algorithms. This was the first all-nighter I ever pulled, and I don't regret it. This project was such a 
              major part of my growth as a programmer and developer, and I still look back at the project fondly to this day. Heck, I might even take another stab at it again one day, but not today.
              I'll leave that to when I'm a much better programmer. <br></br><br></br>

              You can download the .py file <a href="Pygame_Raycasting_Shooter.py" download="Max's Raycasting Engine.py">here</a>.  You will need to have both Python and Pygame installed to run it.
              
              <br></br><br></br><br></br> 

              This is end of the this list of projects. I'll be adding new stuff I do at the top, and hopefully I can look back at this list in 10 years and remember where I started from. 
              There's about a year's gap between these last 2 projects, and while I completed lots projects between them, none are quite big enough to write about and I also can't be bothered 
              to look through all of them. Maybe later, but for now, this'll be fine. 
            </p>
          </div>

        </div>
      </main>

      <footer className={styles.footer}>
        Made using Next.js
        <br></br>Created by Max Zimmermann, 2023
        <br></br>
        <br></br>For business inquiries, email me at max@maxzimmermann.ca
      </footer>
    </div>
  )
}
