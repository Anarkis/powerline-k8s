from powerline_shell.utils import BasicSegment
import subprocess


class Segment(BasicSegment):
    fg_color = 15       # White color
    bg_color = 208      # Orange color

    """
    Add_to_powerline
    Method which will add the kubernetes current context to the powerline
    """
    def add_to_powerline(self):
        k8s_context_command = "kubectl config current-context"
        process = subprocess.Popen(k8s_context_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            self.powerline.append(" " + "*" + " ", self.fg_color, self.bg_color)
        else:
            self.powerline.append(" " + output.decode().replace("\n", "") + " ", self.fg_color, self.bg_color)
