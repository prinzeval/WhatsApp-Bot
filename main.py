from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import threading
import time
import logging
from unread import get_unread_messages, send_messages_to_contacts

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables to manage the background task
monitoring_thread = None
stop_event = threading.Event()

# Message model
class Message(BaseModel):
    text: str

# Background task function to run the monitoring loop
def run_monitoring_loop(message_text: str):
    logger.info("Starting monitoring for unread messages.")
    while not stop_event.is_set():
        start_time = time.time()
        try:
            logger.info("Getting unread messages...")
            contact_names = get_unread_messages()
            
            if contact_names:
                logger.info(f"Sending messages to: {contact_names}")
                send_messages_to_contacts(contact_names, message_text)
                
                # Wait for 2 seconds after sending messages
                logger.info("Waiting for 2 seconds after sending messages.")
                time.sleep(2)
            else:
                logger.info("No unread messages found.")
                
                # Wait for 2 seconds before checking again if no messages were found
                logger.info("Waiting for 2 seconds before next check.")
                time.sleep(2)
        
        except Exception as e:
            logger.error(f"An error occurred: {e}")

        # Adjust sleep duration based on whether messages were sent
        elapsed_time = time.time() - start_time
        sleep_time = max(2 - elapsed_time, 0)
        logger.info(f"Sleeping for {sleep_time} seconds before next check.")
        time.sleep(sleep_time)

@app.post("/start")
async def start_monitoring(message: Message, background_tasks: BackgroundTasks):
    global monitoring_thread, stop_event
    
    if monitoring_thread and monitoring_thread.is_alive():
        return {"message": "Monitoring is already running."}
    
    stop_event.clear()
    
    # Use a background task to start the monitoring loop
    background_tasks.add_task(run_monitoring_loop, message.text)
    
    # Create and start the monitoring thread
    monitoring_thread = threading.Thread(target=run_monitoring_loop, args=(message.text,))
    monitoring_thread.start()
    
    return {"message": "Monitoring started."}

@app.post("/stop")
async def stop_monitoring():
    global stop_event, monitoring_thread
    
    if monitoring_thread and monitoring_thread.is_alive():
        stop_event.set()
        monitoring_thread.join()  # Wait for the thread to finish
        return {"message": "Monitoring stopped."}
    
    return {"message": "Monitoring is not running."}

@app.get("/")
def read_root():
    return {"message": "Welcome to the WhatsApp bot API. Use /start to begin monitoring and /stop to end it."}
