from pytube import YouTube
from alive_progress import alive_bar

# functions 
def n_urls_input(urls):
    while True:
        url = input("enter your url: ")
        if url in "no":
            break
        urls.append(url)


def video_info(url):
    video = YouTube(url)
    print("video title = "+video.title)
    print("video length = "+str(video.length))
    print("author = "+video.author)
    print("publish date = "+str(video.publish_date))
    print("total views = "+str(video.views))
    print("age restriction is set to "+str(video.age_restricted))
    print("video description :\n "+video.description)


def find_quality(p):
    ch1 = ""
    ch = str(p)
    x,y = ch.find("res="),ch.find("fps=")
    for i in range(x+4,y):
        ch1 += ch[i]
    return (ch1)


# main programme
def run():
    urls = []
    quality = []

    n_urls_input(urls)

    for url in urls:
        video = YouTube(url)
        video_info(url)
        print("highest quality available is "+find_quality(video.streams.get_highest_resolution()))
        print("lowest quality available is "+find_quality(video.streams.get_lowest_resolution()))

        a = input("enter the quality: ")
        
        quality.append(a)

    try:
        with alive_bar(len(urls)) as bar:
            for i in range(len(urls)):
                video = YouTube(urls[i])
                if quality[i] == 'audio':
                    video = video.streams.get_audio_only()
                else:
                    video = video.streams.get_by_resolution(quality[i])
                video.download()
                bar()
                print("the video number{0} is downloaded!".format(i+1))
        if len(urls)>1:
            print("all videos are downloaded!")
        elif len(urls)==1:
            print("the video is downloaded!")
        else:
            print("error!")
    except:
        print("\nthere was an error!")
        print("invalid quality choice!")

run()
input("press any key to exit")
