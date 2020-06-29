import psutil
import logging


class Process:
    def __init__(self):
        self.process = None

    def start(self, process_id=None):
        """
        This definition allows to start a new process or instantiate the process already running to psutil.Process().
        :param process_id: Optional
        :return:
        """
        try:
            self.process = psutil.Process(process_id)
            logging.debug(self.process.connections())
            logging.debug(self.process.ppid())
            return "Process Started"
        except Exception as e:
            logging.exception(e)
            return "Process doesnt exists"

    def terminate(self):
        """
        This definition allows to terminate an ongoing process or paused process.
        :return:
        """
        try:
            self.process.terminate()
            return "Process Terminated Successfully"
        except Exception as e:
            logging.exception(e)
            return "Failed to Terminate process"

    def pause(self):
        """
        This definition allows to pause the running process.
        :return:
        """
        try:
            if self.process.status() == "stopped":
                return "Process is already stopped"
            self.process.suspend()
            return "Process Paused Successfully"
        except Exception as e:
            logging.exception(e)
            return "Failed to Pause Process"

    def resume(self, process_id):
        """
        This definition allows to resume the paused process.
        :param process_id:Mandatory
        :return:
        """
        try:
            if self.process.status() == "running":
                return "Process is already running."
            self.process.resume()
            return "Process Resumed Successfully"
        except Exception as e:
            logging.exception(e)
            return "Failed to Resume Process"
