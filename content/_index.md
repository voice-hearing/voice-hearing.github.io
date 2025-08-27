---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "3rem"

sections:
  
  - block: hero1
    content:
      title: Rebirth in Our Community
      text: Bringing Freedom, Peace, and New Life to South-East Birmingham
      secondary: Extending Christ’s love to those marginalized by age, ethnicity, disability, or destitution
      primary_action:
        text: Donate Now - Transform Lives
        url: /donate
        icon: rocket-launch
      secondary_action:
        text: Discover our Story
        url: /about
      announcement:
        text: "Imagine the lives you transform by donating today."
        link:
          text: ""
          url: ""
    design:
      spacing:
        padding: [0, 0, 0, 0]
        margin: [0, 0, 0, 0]
      # For full-screen, add `min-h-screen` below
      css_class: ""
      background: 
        color: ""
        image:
          # Add your image background to `assets/media/`.
          filename: "hero.webp"
          filters:
            brightness: "50%"
  - block: hero-features
    id: hero-features-section
    content:
      # Header Section
      title: "We Care and Share"
      blue: "OUR COMMUNITY"
      text: "Sink into the warm blanket of being loved."
      # LEFT COLUMN: Hero Image with Overlay
      hero:
        title: "Interfaith Accommodation"
        content: ""
        background:
          image:
            filename: "musaf.jpg"  # Place in assets/media/
            filters:
              brightness: "100%"
        align: "bottom"  # top, center, bottom
        text_bg_color: "blue-900/90"  # "blue-900/90" "red-900/85" "green-800/90" "purple-900/95"
        url: "/what-we-do"
        external: false
       # button:
       # text: ""
       # url: ""
       # external: false
      features:
        - name: "Building Bonds Across Faiths"
          description: "As you enter this welcoming space, you may begin to sense how reaching out between faiths gently nurtures new bonds—allowing our whole community to grow closer in understanding."
          icon: "hero/bolt"
          # button:
          #  text: "Learn More"
          #  url: "/performance"            
        - name: "Cultivating charity and Belonging"
          description: "Sometimes, simply sharing a moment of kindness opens doors where charity and respect naturally blossom, helping each person experience deeper well-being and the warmth of true belonging."
          icon: "hero/shield-check"
          # button:
          #   text: "Security Details"
          #   url: "/security"          
        - name: "Inspiring Growth Through Unity"
          description: "By joining these conversations, you might discover how every encounter quietly inspires personal and spiritual growth, inviting all to flourish in a spirit of unity and openness."
          icon: "hero/chart-bar"
          # button:
          #  text: "Contact Support"
          #  url: "/support"         
    design:
      spacing:
        padding: ["2rem", "1rem", "2rem", "1rem"]
  - block: image-overlay
    content:
      slides:
      - title: Hope Garden
        content: 
        align: "bottom"
        url: /what-we-do
        background:
          image:
            filename: "hopegarden1.jpg"
            # filters:
            #    brightness: "1.5"
            # position: center
            # color: '#333'
      - title: Children's Club
        content: 
        align: "bottom"
        url: /what-we-do
        background:
          image:
            filename: "childrensclub1.jpg"
            # filters:
            #    brightness: 0
            # position: center
            # color: '#333'
      - title: Ladies' Day
        content: 
        align: "bottom"
        url: /what-we-do
        background:
          image:
            filename: "ladiesday1.jpg"
            # filters:
            #   brightness: 0
            # position: center
            # color: '#333'
    design:
      spacing:
        padding: [0, 0, 0, 0]
        margin: [0, 0, 0, 0]
      # For full-screen, add `min-h-screen` below
      css_class: ""
      background:
        color: ""
        image:
#          # Add your image background to `assets/media/`.
          filename: ""
          filters:
            brightness:
  - block: cta-image-left-double
    id: features
    content:
      blue: 
      title: 
      text: 
      items:
        - name: 
          image: hopegarden.jpg
          url: https://google.com
          icon:
          description: 
        - name: 
          image: ladiesday.jpg
          url: https://google.com
          icon: 
          description: 
        - name: 
          image: childrensclub.jpg
          url: https://google.com
          description: 
    design:
      spacing:
        padding: [0, 0, 0, 0]
        margin: [0, 0, 0, 0]
      # For full-screen, add `min-h-screen` below
      css_class: ""
      background:
        color: ""
        image:
#          # Add your image background to `assets/media/`.
          filename: ""
          # filters:
          #  brightness: 1
  - block: markdown-quote
    content:
      title: ''
      subtitle: ''
      text: |-
        <p class= "text-gray-800 text-white px-2 text-2xl text-center">
        “Sometimes, you might begin to realize that your generosity today is not only the best choice you can make to transform lives in our community… and as you give, you may notice how, in a very real way, you are gently transforming yourself too.”        
        </p>
    design:
      spacing:
        padding: [0, 0, 0, 0]
        margin: [0, 0, 0, 0]
      # For full-screen, add `min-h-screen` below
      css_class: "bg-primary-600 dark:bg-primary-900"
      background:
        color: ""
        image:
          # Add your image background to `assets/media/`.
          filename: ""
          filters:
            brightness: 
  - block: testimonies-img
    id: testimonies-img
    content:
      title: "Trusted by Our Community"
      blue: "TESTIMONIALS"
      text: "We Have Found Spark Through Service"
      items:
        - name: "Loise Bald"
          text: "Asumet charity gave me not only the tools but also the courage to rebuild my life. As I took each step forward, I could feel hope returning, knowing I was no longer walking this journey alone."
          description: "Cook"
          image: "luis.jpg"
        - name: "Annabel Reed" 
          text: When I had no one else to turn to, their kindness wrapped around me like a warm embrace. With their help, I found strength I didn’t know I had and began standing tall again inside and out.
          description: "Teacher"
          image: "sofia.jpg"
        - name: "Mohammed Yusuf"
          text: "Through their care, I discovered friends who listened, a community that believed in me, and the courage to start fresh. Giving me hope also gave me back my sense of who I truly am."
          description: "Developer"
          image: "mohammed.jpg"
    design:
      spacing:
        padding: ["1rem", 0, 0, 0]
  - block: resume-skills1
    content:
      blue: 
      title: 
      text: 
      username: Admin
  - block: calendar
    content:
      blue: Activities
      title: Fellowship Gatherings
      name: Come and See
      subtitle: 
      text: |-
        <div class="responsive-iframe">
        <iframe
          src="https://calendar.google.com/calendar/u/0?cid=YW5nZWxsZWNpdGVsQGdtYWlsLmNvbQ"
          frameborder="0"
          scrolling="no"
          allowfullscreen>
        </iframe>
        </div>
    design:
      spacing:
        padding: [0, 0, 0, 0]
        margin: [0, 0, 0, 0]
      # For full-screen, add `min-h-screen` below
      css_class: 
      background:
        color: ""
        image:
          # Add your image background to `assets/media/`.
          filename: ""
          filters:
            brightness:
  - block: stats1
    id: features
    content:
      blue: 
      title: Stats
      text: 
      items:
        - name: Since 1983
          icon: /hero/calendar
          description: We Have Roots and We Will Continue to Serve and Grow
        - name: 4000+
          icon: hero/trophy
          description: People - Every Year Demands Grows Yearly
        - name: Open
          icon: hero/book-open
          description: We Welcome Everyone From All Walks of Life
    design:
      spacing:
        padding: [0 , 0, "3rem", 0]
        margin: [0, 0, 0, 0]
      # For full-screen, add `min-h-screen` below
      css_class: ""
#      background:
#        color: ""
#        image:
#          # Add your image background to `assets/media/`.
#          filename: ""
#          filters:
#            brightness: 1.0
  - block: subscribe
    content:
      blue: Subsribe
      title: Keep in Touch
      text: Many people effortlessly subscribe, and you might find that you're already feeling the same desire.
      name: Stay in touch when the moment feels right.
      role: As you choose to keep in touch—whether you subscribe by email or connect with us on WhatsApp—you may begin to notice how, quite naturally, you’re welcomed into a caring community that’s quietly changing lives, including your own. And as those moments of inspiration and belonging reach you, perhaps you’ll sense how easily hope arrives right where you need it most.
      text_cta: "Sign up to our newsletter 🔥"
      description: I consent to having this website store my submitted information so they can respond to my inquiry. Check <a href="https://follow.it/info/privacy" class="unerline">privacy policy.</a> You must agree before submitting.
      button:
        text: "Stay Connected"
    design:
      spacing:
        padding: [0, 0, 0, 0]
        margin: [0, 0, 0, 0]
      # For full-screen, add `min-h-screen` below
      css_class: "bg-gradient-to-r from-primary-300 to-primary-100 dark:from-primary-800 dark:to-primary-900"
      background:
        color: ""
        image:
          # Add your image background to `assets/media/`.
          filename: ""
          filters:
            brightness: 
  - block: testimonials-many
    id: charity-indicators
    content:
      # Header Content
      title: "OUR TEAM"
      blue: "Trusted by Community"
      text: "We Are Here To Help"
      
      # Customizable Rating System
      stars: 5                    # Number of stars (1-5)
      rating: "5.0"              # Rating score display
      reviews: "10,000+"         # Review count
      # user_count: REMOVED       # No more user badge
      
      # Profile Images with URLs
      items:
        - name: "Sarah Johnson"           # Used for alt text
          image: "luis.jpg"              # From assets/media/
          url: "https://twitter.com/sarah" # Optional: profile/social URL
          external: true                  # Optional: opens in new tab
          
        - name: "Michael Chen"            # Used for alt text  
          image: "sofia.jpg"            # From assets/media/
          url: "https://linkedin.com/in/michael"
          external: true
          
        - name: "Emily Rodriguez"         # Used for alt text
          image: "mohammed.jpg"              # From assets/media/
          url: "/team/emily"              # Internal link (no external needed)
          
        - name: "David Kim"               # Used for alt text
          image: "sofia.jpg"              # From assets/media/
          url: "https://github.com/david"
          external: true
          
        - name: "Lisa Thompson"           # Used for alt text
          image: "luis.jpg"               # From assets/media/
          # url: not required             # Image won't be clickable
  
    design:
      spacing:
        padding: ["1rem", 0, 0, 0]
  - block: contact
    id: contact
    content:
      blue: Contact Us
      title: Communicate Your Needs
      text: “Ask and it will be given to you; seek and you will find; knock and the door will be opened to you."
      text_cta: 
      text_privacy:  I consent to having this website store my submitted information so they can respond to my inquiry. Check <a href="/en/privacy" class="unerline">privacy policy.</a> You must agree before submitting.
      
      phone: 888 888 88 88
      # appointment_url: 'https://calendly.com'
      address:
        street: 450 Serra Mall
        city: Stanford
        region: CA
        postcode: '94305'
        country: United States
        country_code: US
      office_hours:
        - 'Monday 10:00 to 13:00'
        - 'Wednesday 09:00 to 10:00'
    #  directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
    #  email: test@example.org
    #  contact_links:
    #    - icon: twitter
    #      icon_pack: fab
    #      name: DM Me
    #      link: 'https://twitter.com/Twitter'
    #    - icon: skype
    #      icon_pack: fab
    #      name: Skype Me
    #      link: 'skype:echo123?call'
    #    - icon: video
    #      icon_pack: fas
    #      name: Zoom Me
    #      link: 'https://zoom.com'
      # Automatically link email and phone or display them just as text?
      autolink: true
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2' 
---    
    