import streamlit as st
import googleapiclient.discovery
import googleapiclient.errors
from langchain_community.document_loaders import YoutubeLoader
import load

def main():
    api_key = "AIzaSyCYUSC2ZeccGO7ax4FyETv6aSADU-fortU"  # Replace with your API key
    channelMail = st.text_input("Enter channel mail")

    api_service_name = "youtube"
    api_version = "v3"

    # JavaScript to request notification permission on page load
    st.components.v1.html("""
        <script>
            // Request notification permission when the page loads
            document.addEventListener("DOMContentLoaded", function() {
                Notification.requestPermission().then(function(permission) {
                    if (permission === "granted") {
                        console.log("Notification permission granted.");
                    } else if (permission === "denied") {
                        console.log("Notification permission denied.");
                    }
                });
            });
        </script>
    """, height=0)

    # Create an API client
    if st.button("Enter"):
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=api_key
        )

        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            forHandle=channelMail
        )
        response = request.execute()
        
        if "items" in response and len(response["items"]) > 0:
            channelID = response["items"][0]["id"]
            request = youtube.search().list(
                part="snippet",
                channelId=channelID,
                maxResults=1,
                order="date"
            )
            response = request.execute()
            
            videoId = response["items"][0]["id"]["videoId"]
            videoUrl = f"https://www.youtube.com/watch?v={videoId}"
            st.write(videoUrl)

            url = videoUrl
            loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
            transcript = loader.load()
            response = load.output(str(transcript))
            
            for chunk in response:
                st.write(chunk.text)

            # Inject JavaScript to send a notification after summarization with redirection
            st.components.v1.html(f"""
                <script>
                    // Function to send notification
                    function sendNotification() {{
                        if (Notification.permission === "granted") {{
                            let notification = new Notification("Summarization complete!", {{
                                body: "Click to view the summarized video.",
                                icon: "https://example.com/icon.png"  // You can add an icon if needed
                            }});
                            notification.onclick = function() {{
                                window.open("{videoUrl}", "_blank");
                            }};
                        }} else if (Notification.permission !== "denied") {{
                            Notification.requestPermission().then(function(permission) {{
                                if (permission === "granted") {{
                                    let notification = new Notification("Summarization complete!", {{
                                        body: "Click to view the summarized video.",
                                        icon: "https://example.com/icon.png"
                                    }});
                                    notification.onclick = function() {{
                                        window.open("{videoUrl}", "_blank");
                                    }};
                                }}
                            }});
                        }}
                    }}

                    // To Send the notification
                    sendNotification();
                </script>
            """, height=0)

        else:
            st.write("No channel found for the provided email.")

if __name__ == "__main__":
    main()
