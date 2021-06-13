import heapq


def find_min_ticket_price(customers, ships, tickets):
    heapq.heapify(tickets)
    min_cost = 0
    for _ in range(customers):
        val = heapq.heappop(tickets)
        min_cost += val
        val -= 1
        if val:
            heapq.heappush(tickets, val)
    return min_cost


def find_max_ticket_price(customers, ships, tickets):
    tickets = [-1 * i for i in tickets]
    heapq.heapify(tickets)
    max_cost = 0
    for _ in range(customers):
        val = heapq.heappop(tickets)
        max_cost += val
        val += 1
        if val:
            heapq.heappush(tickets, val)
    return -max_cost


if __name__ == '__main__':
    A = 4
    B = 3
    C = [2, 2, 2]
    D = C[:]
    print('*' * 80)
    print('iron man C', C)
    print(find_min_ticket_price(A, B, C))
    print(find_max_ticket_price(A, B, D))
