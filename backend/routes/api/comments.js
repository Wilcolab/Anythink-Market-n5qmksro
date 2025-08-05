// Description: API routes for managing comments

const router = require("express").Router();
const mongoose = require("mongoose");
const Comment = mongoose.model("Comment");

module.exports = router;

router.get("/", async (req, res) => {
    try {
        const comments = await Comment.find().sort({ createdAt: -1 });
        res.status(200).json(comments);
    } catch (error) {
        console.error("Error fetching comments:", error);
        res.status(500).json({ error: "Internal server error" });
    }
    });

// add another endpoint to delete comments
router.delete("/:id", async (req, res) => {
    try {
        const comment = await Comment.findByIdAndDelete(req.params.id);
        if (!comment) {
            return res.status(404).json({ error: "Comment not found" });
        }
        res.status(200).json({ message: "Comment deleted successfully" });
    } catch (error) {
        console.error("Error deleting comment:", error);
        res.status(500).json({ error: "Internal server error" });
    }
    });
