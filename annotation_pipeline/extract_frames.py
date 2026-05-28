import h5py
import cv2
import numpy as np
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path", type=str, required=True)
    parser.add_argument("--output_dir", type=str, default="frames")
    parser.add_argument("--skip", type=int, default=10)

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    with h5py.File(args.file_path, "r") as f:
        human = f["/cam_data/human_camera"]
        robot = f["/cam_data/robot_camera"]

        print("num frames:", len(human))

        for i in range(0, len(human), args.skip):
            h_img = human[i].astype(np.uint8)
            r_img = robot[i].astype(np.uint8)

            h_img = cv2.cvtColor(h_img, cv2.COLOR_RGB2BGR)
            r_img = cv2.cvtColor(r_img, cv2.COLOR_RGB2BGR)

            cv2.imwrite(
                os.path.join(args.output_dir, f"{i:04d}_human.jpg"),
                h_img
            )

            cv2.imwrite(
                os.path.join(args.output_dir, f"{i:04d}_robot.jpg"),
                r_img
            )

    print("Frames saved to:", args.output_dir)

if __name__ == "__main__":
    main()