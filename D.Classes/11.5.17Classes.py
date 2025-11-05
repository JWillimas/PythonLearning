# 17-Good Example of Inheritance

# class InvalidationError(Exception):
#     pass


# class Stream:
#     def __init__(self):
#         self.opend = False

#     # def __str__(self):
#     #     return f"{self.opend}"

#     def open(self):
#         if self.opend:
#             raise InvalidationError("stream is already open")
#         self.opend = True

#     def close(self):
#         if not self.opend:
#             raise InvalidationError("stream is already close")
#         self.opend = False


# stream01 = Stream()
# stream02 = Stream()
# stream01.open()

# print(stream01.opend)
# print(stream02.opend)
