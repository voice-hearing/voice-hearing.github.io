---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "3rem"

sections:
  
  - block: hero
    content:
      title: Rebirth in Our Community
      text: Bringing Freedom, Peace, and New Life to South-East Birmingham
      secondary: Extending Christ’s love to those marginalized by age, ethnicity, disability, or destitution
      primary_action:
        text: Donate Now - Transform Lives
        url: /en/donate
        icon: rocket-launch
      secondary_action:
        text: Discover our Story
        url: /en/about
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
  - block: cta-img-bullets
    id: features
    content:
      blue: 
      title:
      text: 
      items:
        - name: 
          image: house.jpg
          url: /en/what-we-do/
          description: 
        - subtitle: 
          role: 
          name: Building Bonds Across Faiths
          icon: /custom/wholeness
          description: As you enter this welcoming space, you may begin to sense how reaching out between faiths gently nurtures new bonds—allowing our whole community to grow closer in understanding.
        - name: Cultivating Trust and Belonging
          icon: /custom/wholeness
          description: Sometimes, simply sharing a moment of kindness opens doors where trust and respect naturally blossom, helping each person experience deeper well-being and the warmth of true belonging.
        - name: Inspiring Growth Through Unity
          icon: /custom/wholeness
          description: By joining these conversations, you might discover how every encounter quietly inspires personal and spiritual growth, inviting all to flourish in a spirit of unity and openness.
          button:
            text:
            url: 
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
            brightness: 0.5
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
          filters:
            brightness: 0.5
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
      css_class: "bg-gradient-to-r from-primary-500 to-primary-600 dark:from-primary-800 dark:to-primary-900"
      background:
        color: ""
        image:
          # Add your image background to `assets/media/`.
          filename: ""
          filters:
            brightness: 
  - block: testimonies-img
    content:
      title: 
      blue: 
      text: 
      items:
        - name: John Bald
          text: Azumi Trust gave me not only the tools but also the courage to rebuild my life. As I took each step forward, I could feel hope returning, knowing I was no longer walking this journey alone.
          description: Cook
          # Upload image to `assets/media/` and reference the filename here
          image: luis.webp
        - name: Annabel Reed
          text: When I had no one else to turn to, their kindness wrapped around me like a warm embrace. With their help, I found strength I didn’t know I had and began standing tall again inside and out.
          description: Teacher
          # Upload image to `assets/media/` and reference the filename here
          image: sonia.webp
        - name: Mohammed Yusuf
          text: Through their care, I discovered friends who listened, a community that believed in me, and the courage to start fresh. Giving me hope also gave me back my sense of who I truly am.
          description: "Father and Mechanic"
          # Upload image to `assets/media/` and reference the filename here
          image: "joaquin.webp"
    design:
      spacing:
        # Reduce bottom spacing so the testimonial appears vertically centered between sections
        padding: ["1rem", 0, 0, 0]
  - block: skills
    content:
      blue: 
      title: 
      text: 
      username: Admin
  - block: calendar
    content:
      title: Fellowship Gatherings
      subtitle: 
      text: |-
        <div class="responsive-iframe">
        <iframe
          src="https://calendar.google.com/calendar/embed?height=600&wkst=2&ctz=Europe%2FLondon&hl=en_GB&src=ZW4uY2hyaXN0aWFuI2hvbGlkYXlAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&color=%234285f4"
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
          description: We Will Continue
        - name: 100+ People
          icon: hero/trophy
          description: Demands Grows Yearly
        - name: To Everyone
          icon: hero/book-open
          description: We Are Open
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
      blue: 
      title: Keep in Touch
      text: As you choose to keep in touch—whether you subscribe by email or connect with us on WhatsApp—you may begin to notice how, quite naturally, you’re welcomed into a caring community that’s quietly changing lives, including your own. And as those moments of inspiration and belonging reach you, perhaps you’ll sense how easily hope arrives right where you need it most.
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
    id: trust-indicators
    content:
      # Header Content
      title: "Trusted by People"
      blue: "OUR TEAM"
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
          image: "luis.jpg"            # From assets/media/
          url: "https://linkedin.com/in/michael"
          external: true
          
        - name: "Emily Rodriguez"         # Used for alt text
          image: "luis.jpg"              # From assets/media/
          url: "/team/emily"              # Internal link (no external needed)
          
        - name: "David Kim"               # Used for alt text
          image: "luis.jpg"              # From assets/media/
          url: "https://github.com/david"
          external: true
          
        - name: "Lisa Thompson"           # Used for alt text
          image: "luis.jpg"               # From assets/media/
          # url: not required             # Image won't be clickable
  
    design:
      spacing:
        padding: ["1rem", 0, 0, 0]
---    
    